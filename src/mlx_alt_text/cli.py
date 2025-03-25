import click

from pathlib import Path

from .generator import AltTextGenerator


@click.command()
@click.argument(
    "image_path",
    type=click.Path(exists=True, file_okay=True, dir_okay=False, path_type=Path),
)
def alt_text(image_path: Path):
    """Generate alt-text for the provided iamge using local MLX models."""
    generator = AltTextGenerator()
    try:
        result = generator.generate(
            "What's in this image?", image=image_path.absolute().as_posix()
        )
        click.echo(result)
    except Exception as e:
        click.echo(f"Error generating alt-text: {e}", err=True)
        raise click.Abort()


def main():
    alt_text()


if __name__ == "__main__":
    main()
