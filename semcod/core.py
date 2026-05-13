"""
Core classes for the harp package.
"""

import numpy as np
from typing import List
from .utils import note_to_frequency


class HarpString:
    """Represents a single harp string with its properties and behavior."""

    def __init__(self, note: str, length: float = 1.0, tension: float = 100.0):
        """
        Initialize a harp string.

        Args:
            note: Musical note (e.g., 'C4', 'A4')
            length: String length in meters
            tension: String tension in Newtons
        """
        self.note = note
        self.frequency = note_to_frequency(note)
        self.length = length
        self.tension = tension
        self.is_vibrating = False
        self.amplitude = 0.0
        self.phase = 0.0

    def pluck(self, velocity: float = 0.8) -> None:
        """
        Pluck the string with given velocity.

        Args:
            velocity: Plucking velocity (0.0 to 1.0)
        """
        self.is_vibrating = True
        self.amplitude = min(velocity, 1.0)
        self.phase = 0.0

    def stop(self) -> None:
        """Stop the string vibration."""
        self.is_vibrating = False
        self.amplitude = 0.0

    def get_sample(self, sample_rate: int = 44100, time: float = 0.0) -> float:
        """
        Get the current sample value for this string.

        Args:
            sample_rate: Audio sample rate
            time: Current time in seconds

        Returns:
            Sample value between -1.0 and 1.0
        """
        if not self.is_vibrating:
            return 0.0

        # Simple sine wave with exponential decay
        decay_rate = 2.0  # Decay constant
        decay = np.exp(-decay_rate * time)
        sample = (
            self.amplitude
            * decay
            * np.sin(2 * np.pi * self.frequency * time + self.phase)
        )

        # Stop vibrating if amplitude is too small
        if abs(sample) < 0.001:
            self.stop()

        return sample


class Harp:
    """Represents a harp instrument with multiple strings."""

    def __init__(self, num_strings: int = 47):
        """
        Initialize a harp with specified number of strings.

        Args:
            num_strings: Number of strings on the harp
        """
        self.num_strings = num_strings
        self.strings: List[HarpString] = []
        self.sample_rate = 44100

    def tune_to_standard(self) -> None:
        """Tune the harp to standard diatonic scale."""
        # Standard harp tuning from C1 to C7 (diatonic)
        notes = []
        for octave in range(1, 8):
            for note_name in ["C", "D", "E", "F", "G", "A", "B"]:
                notes.append(f"{note_name}{octave}")

        # Take only the first num_strings notes
        notes = notes[: self.num_strings]

        self.strings = []
        for note in notes:
            # Vary string length slightly for realism
            length = 1.0 + (len(self.strings) * 0.01)
            string = HarpString(note, length=length)
            self.strings.append(string)

    def pluck_string(self, string_index: int, velocity: float = 0.8) -> None:
        """
        Pluck a specific string.

        Args:
            string_index: Index of the string to pluck
            velocity: Plucking velocity (0.0 to 1.0)
        """
        if 0 <= string_index < len(self.strings):
            self.strings[string_index].pluck(velocity)

    def stop_string(self, string_index: int) -> None:
        """
        Stop a specific string from vibrating.

        Args:
            string_index: Index of the string to stop
        """
        if 0 <= string_index < len(self.strings):
            self.strings[string_index].stop()

    def stop_all(self) -> None:
        """Stop all strings from vibrating."""
        for string in self.strings:
            string.stop()

    def get_sample(self, time: float = 0.0) -> float:
        """
        Get the current sample value for all strings combined.

        Args:
            time: Current time in seconds

        Returns:
            Combined sample value
        """
        total_sample = 0.0
        for string in self.strings:
            total_sample += string.get_sample(self.sample_rate, time)

        # Normalize to prevent clipping
        return np.clip(total_sample / len(self.strings), -1.0, 1.0)

    def generate_audio(self, duration: float = 1.0) -> np.ndarray:
        """
        Generate audio data for the current state.

        Args:
            duration: Duration in seconds

        Returns:
            NumPy array of audio samples
        """
        num_samples = int(self.sample_rate * duration)
        audio = np.zeros(num_samples)

        for i in range(num_samples):
            time = i / self.sample_rate
            audio[i] = self.get_sample(time)

        return audio
