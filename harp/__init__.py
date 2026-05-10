"""
Harp - A Python package for musical string manipulation and analysis.

This package provides tools for working with musical concepts,
particularly focused on harp-like string instruments and their properties.
"""

__version__ = "0.1.5"
__author__ = "Your Name"
__email__ = "your.email@example.com"

from .core import HarpString, Harp
from .utils import note_to_frequency, frequency_to_note

__all__ = [
    "HarpString",
    "Harp", 
    "note_to_frequency",
    "frequency_to_note"
]
