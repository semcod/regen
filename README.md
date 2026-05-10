# Harp


## AI Cost Tracking

![PyPI](https://img.shields.io/badge/pypi-costs-blue) ![Version](https://img.shields.io/badge/version-0.1.2-blue) ![Python](https://img.shields.io/badge/python-3.9+-blue) ![License](https://img.shields.io/badge/license-Apache--2.0-green)
![AI Cost](https://img.shields.io/badge/AI%20Cost-$0.15-orange) ![Human Time](https://img.shields.io/badge/Human%20Time-2.0h-blue) ![Model](https://img.shields.io/badge/Model-openrouter%2Fqwen%2Fqwen3--coder--next-lightgrey)

- 🤖 **LLM usage:** $0.1500 (1 commits)
- 👤 **Human dev:** ~$200 (2.0h @ $100/h, 30min dedup)

Generated on 2026-05-10 using [openrouter/qwen/qwen3-coder-next](https://openrouter.ai/qwen/qwen3-coder-next)

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
