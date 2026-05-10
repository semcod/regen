"""
Command line interface for the harp package.
"""

import argparse
import numpy as np
import soundfile as sf
from .core import Harp
from .utils import note_to_frequency


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(description="Harp - Musical string manipulation tool")
    parser.add_argument("--generate", "-g", action="store_true", 
                       help="Generate audio from harp")
    parser.add_argument("--notes", "-n", nargs="+", default=["C4", "E4", "G4"],
                       help="Notes to play (e.g., C4 E4 G4)")
    parser.add_argument("--duration", "-d", type=float, default=2.0,
                       help="Duration in seconds")
    parser.add_argument("--output", "-o", default="harp_output.wav",
                       help="Output audio file")
    parser.add_argument("--strings", "-s", type=int, default=47,
                       help="Number of strings on the harp")
    parser.add_argument("--sample-rate", type=int, default=44100,
                       help="Audio sample rate")
    
    args = parser.parse_args()
    
    if args.generate:
        generate_harp_audio(args)
    else:
        parser.print_help()


def generate_harp_audio(args):
    """Generate harp audio and save to file."""
    print(f"Creating harp with {args.strings} strings...")
    harp = Harp(num_strings=args.strings)
    harp.tune_to_standard()
    harp.sample_rate = args.sample_rate
    
    print(f"Playing notes: {', '.join(args.notes)}")
    
    # Play each note with a slight delay
    note_delay = 0.1  # seconds between notes
    total_duration = args.duration + len(args.notes) * note_delay
    
    # Generate audio
    audio = harp.generate_audio(total_duration)
    
    # Add notes at different times
    for i, note in enumerate(args.notes):
        # Find the string that matches this note
        string_index = None
        for j, string in enumerate(harp.strings):
            if string.note == note:
                string_index = j
                break
        
        if string_index is not None:
            # Pluck the string at the appropriate time
            start_time = i * note_delay
            start_sample = int(start_time * args.sample_rate)
            
            # Generate audio for this note and add it
            harp.pluck_string(string_index, velocity=0.8)
            note_audio = harp.generate_audio(args.duration)
            
            # Add to main audio at the right position
            end_sample = min(start_sample + len(note_audio), len(audio))
            note_samples = end_sample - start_sample
            if note_samples > 0:
                audio[start_sample:end_sample] += note_audio[:note_samples]
            
            harp.stop_all()
        else:
            print(f"Warning: Note {note} not found on harp")
    
    # Normalize audio
    audio = np.clip(audio / np.max(np.abs(audio)), -1.0, 1.0)
    
    # Save to file
    print(f"Saving audio to {args.output}...")
    sf.write(args.output, audio, args.sample_rate)
    print("Done!")


if __name__ == "__main__":
    main()
