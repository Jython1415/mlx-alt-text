# MLX Alt Text

ARCHIVED! This project is being archived because I don't expect this niche to be valuable for long, and I don't intend to continue to improve the project. It was a great learning experience though, and that was the whole point.

A Python package for generating alt-text for images using local MLX models.

## About

MLX Alt Text is a local-first alt-text generator built on top of MLX-VLM. It allows you to generate descriptive alt-text for images using vision-language models that run entirely on your device using Apple's MLX framework.

## Features

- Generate detailed accessibility descriptions for images
- Run entirely on-device (no network usage except to download the model)
- Customizable prompts, output lengths, and temperatures
- Command-line interface for easy integration into workflows
- Python API for integration into your applications

## Requirements

- macOS with Apple Silicon

## Installation

```bash
uv tool install mlx-alt-text # CLI installation with uv (recommended)
pipx install mlx-alt-text    # CLI installation with pipx
pip install mlx-alt-text     # Python pacakge installation
```

## Usage

### Command-line Interface

Generate alt-text for an image:

```bash
mlx-alt-text generate path/to/image.jpg
```

With custom options:

```bash
mlx-alt-text generate path/to/image.jpg \
  --prompt "Describe this image in detail for accessibility purposes" \
  --model <path-to-model-snapshot> \
  --max-tokens 150 \
  --temperature 0.3
```

### Python API

```python
from mlx_alt_text import AltTextGenerator

# Initialize with default options
generator = AltTextGenerator()

# Or with custom options
generator = AltTextGenerator(
    model_path="<path-to-model-snapshot",
    max_tokens=100,
    temperature=0.2
)

# Generate alt-text
alt_text = generator.generate(
    image="path/to/image.jpg",
    prompt="Describe this image for accessibility purposes"
)

print(alt_text)
```

## Development Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/mlx-alt-text.git
cd mlx-alt-text
```

2. Set up the development environment with uv:

```bash
# Install uv if you don't have it
curl -LsSf https://astral.sh/uv/install.sh | sh

# Create a virtual environment and install dependencies
uv sync
source .venv/bin/activate
uv run mlx-alt-text
```

3. Run tests:

```bash
pytest
```

## Acknowledgement

I was inspired to try this project after using [Simon Willison](https://simonwillison.net)'s [`llm` package](https://llm.datasette.io/en/stable/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

