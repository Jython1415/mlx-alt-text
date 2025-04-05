from pathlib import Path

import click

from .constants import DEFAULT_MAX_TOKENS, DEFAULT_TEMPERATURE
from .generator import AltTextGenerator
from .model_utils import download_model


@click.group(
    invoke_without_command=True,
    context_settings={"help_option_names": ["-h", "--help"]},
)
def cli():
    """MLX Alt-Text: Generate accessible image descriptions using local MLX models."""
    pass


@cli.command("generate")
@click.argument(
    "image_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
@click.option(
    "--model",
    "-m",
    type=click.Path(exists=True, file_okay=False, dir_okay=True, path_type=Path),
    help="The path to the model to use for generation. The exact snapshot must be specified as well.",
)
@click.option(
    "--prompt",
    "-p",
    default="Describe this image in detail for accessibility purposes",
    help="Custom prompt to use for generation",
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
def generate(image_path, prompt, model, max_tokens, temperature, verbose):
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


@cli.command("download")
@click.argument("model_name")
@click.option("--verbose", "-v", is_flag=True, help="Enable verbose output")
def download(model_name, verbose):
    """Download a model for later use with the generate command."""
    try:
        path = download_model(model_name, verbose=verbose)
        click.echo(f"Model successfully downloaded to: {path}")
    except Exception as e:
        click.echo(f"Error downloading model: {e}", err=True)
        raise click.Abort()


def main():
    cli()


if __name__ == "__main__":
    main()
