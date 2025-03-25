from pathlib import Path

import click

from .constants import *
from .generator import AltTextGenerator


@click.command()
@click.argument(
    "image_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
@click.option(
    "--prompt",
    "-p",
    default="Describe this image in detail for accessibility purposes",
    help="Custom prompt to use for generation",
)
@click.option(
    "--model",
    "-m",
    default=DEFAULT_MODEL,
    help="Model to use for generation, try 'mlx-community/SmolVLM-Instruct-bf16' or 'mlx-community/SmolVLM-256M-Instruct-4bit'",
)
@click.option(
    "--max-tokens",
    type=int,
    default=DEFAULT_MAX_TOKENS,
    help="Maximum tokens to generate",
)
@click.option(
    "--temperature",
    type=float,
    default=DEFAULT_TEMPERATURE,
    help="Temperature for generation",
)
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def alt_text(image_path, prompt, model, max_tokens, temperature, verbose):
    """Generate alt-text for the provided iamge using local MLX models."""
    generator = AltTextGenerator(model, max_tokens, temperature)
    try:
        result = generator.generate(
            image_path.absolute().as_posix(), prompt, verbose=verbose
        )
        click.echo(result)
    except Exception as e:
        click.echo(f"Error generating alt-text: {e}", err=True)
        raise click.Abort()


def main():
    alt_text()


if __name__ == "__main__":
    main()
