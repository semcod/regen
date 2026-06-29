# Harp


## AI Cost Tracking

![AI Cost](https://img.shields.io/badge/AI%20Cost-$0.13-brightgreen) ![AI Model](https://img.shields.io/badge/AI%20Model-openrouter%2Fdeep%2Fdeep-v4-pro-lightgrey)

This project uses AI-generated code. Total cost: **$0.1307** with **10** AI commits.

Generated on 2026-06-29 using [openrouter/deep/deep-v4-pro](https://openrouter.ai/models/openrouter/deep/deep-v4-pro)

---

A Python package for musical string manipulation and analysis, particularly focused on harp-like string instruments and their properties.

## Features

- Musical note and frequency conversion utilities
- String vibration modeling
- Harp instrument simulation
- Audio analysis tools for string instruments

## Installation

```bash
pip install harp
```

## Quick Start

```python
from harp import Harp, note_to_frequency, frequency_to_note

# Convert between notes and frequencies
freq = note_to_frequency('A4')
note = frequency_to_note(440.0)

# Create a harp with standard tuning
harp = Harp(num_strings=47)
harp.tune_to_standard()

# Play a note
harp.pluck_string(0, velocity=0.8)
```

## Development

Install in development mode:

```bash
git clone https://github.com/yourusername/harp.git
cd harp
pip install -e .[dev]
```

This package uses modern Python packaging with `pyproject.toml`. No `setup.py` file is required.

Run tests:

```bash
pytest
```

## License

Licensed under Apache-2.0.
