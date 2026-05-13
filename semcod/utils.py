"""
Utility functions for the harp package.
"""

import numpy as np
from typing import Dict


# Standard note frequencies (A4 = 440 Hz tuning)
NOTE_FREQUENCIES: Dict[str, float] = {
    "C0": 16.35,
    "C#0": 17.32,
    "D0": 18.35,
    "D#0": 19.45,
    "E0": 20.60,
    "F0": 21.83,
    "F#0": 23.12,
    "G0": 24.50,
    "G#0": 25.96,
    "A0": 27.50,
    "A#0": 29.14,
    "B0": 30.87,
    "C1": 32.70,
    "C#1": 34.65,
    "D1": 36.71,
    "D#1": 38.89,
    "E1": 41.20,
    "F1": 43.65,
    "F#1": 46.25,
    "G1": 49.00,
    "G#1": 51.91,
    "A1": 55.00,
    "A#1": 58.27,
    "B1": 61.74,
    "C2": 65.41,
    "C#2": 69.30,
    "D2": 73.42,
    "D#2": 77.78,
    "E2": 82.41,
    "F2": 87.31,
    "F#2": 92.50,
    "G2": 98.00,
    "G#2": 103.83,
    "A2": 110.00,
    "A#2": 116.54,
    "B2": 123.47,
    "C3": 130.81,
    "C#3": 138.59,
    "D3": 146.83,
    "D#3": 155.56,
    "E3": 164.81,
    "F3": 174.61,
    "F#3": 185.00,
    "G3": 196.00,
    "G#3": 207.65,
    "A3": 220.00,
    "A#3": 233.08,
    "B3": 246.94,
    "C4": 261.63,
    "C#4": 277.18,
    "D4": 293.66,
    "D#4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "G4": 392.00,
    "G#4": 415.30,
    "A4": 440.00,
    "A#4": 466.16,
    "B4": 493.88,
    "C5": 523.25,
    "C#5": 554.37,
    "D5": 587.33,
    "D#5": 622.25,
    "E5": 659.25,
    "F5": 698.46,
    "F#5": 739.99,
    "G5": 783.99,
    "G#5": 830.61,
    "A5": 880.00,
    "A#5": 932.33,
    "B5": 987.77,
    "C6": 1046.50,
    "C#6": 1108.73,
    "D6": 1174.66,
    "D#6": 1244.51,
    "E6": 1318.51,
    "F6": 1396.91,
    "F#6": 1479.98,
    "G6": 1567.98,
    "G#6": 1661.22,
    "A6": 1760.00,
    "A#6": 1864.66,
    "B6": 1975.53,
    "C7": 2093.00,
    "C#7": 2217.46,
    "D7": 2349.32,
    "D#7": 2489.02,
    "E7": 2637.02,
    "F7": 2793.83,
    "F#7": 2959.96,
    "G7": 3135.96,
    "G#7": 3322.44,
    "A7": 3520.00,
    "A#7": 3729.31,
    "B7": 3951.07,
    "C8": 4186.01,
    "C#8": 4434.92,
    "D8": 4698.63,
    "D#8": 4978.03,
    "E8": 5274.04,
    "F8": 5587.65,
    "F#8": 5919.91,
    "G8": 6271.93,
    "G#8": 6644.88,
    "A8": 7040.00,
    "A#8": 7458.62,
    "B8": 7902.13,
}

# Note names in order
NOTE_NAMES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def note_to_frequency(note: str) -> float:
    """
    Convert a musical note to its frequency in Hz.

    Args:
        note: Musical note in scientific pitch notation (e.g., 'A4', 'C#3')

    Returns:
        Frequency in Hz

    Raises:
        ValueError: If note format is invalid
    """
    if note not in NOTE_FREQUENCIES:
        raise ValueError(f"Invalid note: {note}")
    return NOTE_FREQUENCIES[note]


def frequency_to_note(frequency: float) -> str:
    """
    Convert a frequency to the closest musical note.

    Args:
        frequency: Frequency in Hz

    Returns:
        Closest musical note in scientific pitch notation

    Raises:
        ValueError: If frequency is out of valid range
    """
    if frequency <= 0:
        raise ValueError("Frequency must be positive")

    # Find the closest note
    closest_note = None
    min_distance = float("inf")

    for note, note_freq in NOTE_FREQUENCIES.items():
        distance = abs(note_freq - frequency)
        if distance < min_distance:
            min_distance = distance
            closest_note = note

    if closest_note is None:
        raise ValueError("Frequency out of range")

    return closest_note


def frequency_to_midi_note(frequency: float) -> int:
    """
    Convert frequency to MIDI note number.

    Args:
        frequency: Frequency in Hz

    Returns:
        MIDI note number (0-127)
    """
    if frequency <= 0:
        raise ValueError("Frequency must be positive")

    # A4 = 440 Hz = MIDI note 69
    midi_note = int(round(12 * np.log2(frequency / 440.0) + 69))
    return np.clip(midi_note, 0, 127)


def midi_note_to_frequency(midi_note: int) -> float:
    """
    Convert MIDI note number to frequency.

    Args:
        midi_note: MIDI note number (0-127)

    Returns:
        Frequency in Hz
    """
    if not (0 <= midi_note <= 127):
        raise ValueError("MIDI note must be between 0 and 127")

    # A4 = 440 Hz = MIDI note 69
    return 440.0 * (2 ** ((midi_note - 69) / 12))


def get_scale_notes(root: str, scale_type: str = "major") -> list:
    """
    Get notes for a musical scale starting from root note.

    Args:
        root: Root note (e.g., 'C4')
        scale_type: Type of scale ('major', 'minor', 'pentatonic', etc.)

    Returns:
        List of notes in the scale
    """
    # Scale intervals (semitones from root)
    scale_intervals = {
        "major": [0, 2, 4, 5, 7, 9, 11],
        "minor": [0, 2, 3, 5, 7, 8, 10],
        "pentatonic_major": [0, 2, 4, 7, 9],
        "pentatonic_minor": [0, 3, 5, 7, 10],
        "blues": [0, 3, 5, 6, 7, 10],
        "chromatic": list(range(12)),
    }

    if scale_type not in scale_intervals:
        raise ValueError(f"Unknown scale type: {scale_type}")

    # Extract root note name and octave
    if len(root) < 2:
        raise ValueError("Invalid root note format")

    note_name = root[:-1]
    octave = int(root[-1])

    # Find root note index
    try:
        root_index = NOTE_NAMES.index(note_name)
    except ValueError:
        raise ValueError(f"Invalid note name: {note_name}")

    # Generate scale notes
    scale_notes = []
    intervals = scale_intervals[scale_type]

    for interval in intervals:
        note_index = (root_index + interval) % 12
        octave_offset = (root_index + interval) // 12
        new_octave = octave + octave_offset
        scale_note = f"{NOTE_NAMES[note_index]}{new_octave}"
        scale_notes.append(scale_note)

    return scale_notes


def apply_envelope(
    signal: np.ndarray,
    attack: float = 0.1,
    decay: float = 0.2,
    sustain: float = 0.7,
    release: float = 0.3,
    sample_rate: int = 44100,
) -> np.ndarray:
    """
    Apply ADSR envelope to audio signal.

    Args:
        signal: Input audio signal
        attack: Attack time in seconds
        decay: Decay time in seconds
        sustain: Sustain level (0.0 to 1.0)
        release: Release time in seconds
        sample_rate: Audio sample rate

    Returns:
        Envelope-applied signal
    """
    signal_length = len(signal)
    envelope = np.ones(signal_length)

    # Convert times to samples
    attack_samples = int(attack * sample_rate)
    decay_samples = int(decay * sample_rate)
    release_samples = int(release * sample_rate)

    # Attack phase
    if attack_samples > 0:
        attack_samples = min(attack_samples, signal_length)
        envelope[:attack_samples] = np.linspace(0, 1, attack_samples)

    # Decay phase
    if decay_samples > 0:
        decay_start = attack_samples
        decay_end = min(decay_start + decay_samples, signal_length)
        if decay_end > decay_start:
            envelope[decay_start:decay_end] = np.linspace(
                1, sustain, decay_end - decay_start
            )

    # Sustain phase
    sustain_start = attack_samples + decay_samples
    sustain_end = max(signal_length - release_samples, sustain_start)
    if sustain_end > sustain_start:
        envelope[sustain_start:sustain_end] = sustain

    # Release phase
    if release_samples > 0:
        release_start = signal_length - release_samples
        if release_start > 0:
            envelope[release_start:] = np.linspace(
                envelope[release_start], 0, release_samples
            )

    return signal * envelope
