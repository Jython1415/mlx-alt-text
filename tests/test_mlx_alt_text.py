from pathlib import Path

import pytest
import mlx_alt_text
from mlx_alt_text import AltTextGenerator

# This model is ~512MB
# https://huggingface.co/mlx-community/SmolVLM-256M-Instruct-bf16
# TODO This model must be downloaded and available for these tests to work
TINY_MODEL = "~/.cache/huggingface/hub/models--mlx-community--SmolVLM-256M-Instruct-bf16/snapshots/cfe17933371986666073f450510d9e40d6157b13"
TINY_IMAGE = Path("tests/penguin-image.png")


@pytest.fixture(scope="module")
def alt_text_generator():
    """Creates a single instance of AltTextGenerator."""
    generator = AltTextGenerator(TINY_MODEL)
    assert isinstance(generator, mlx_alt_text.AltTextGenerator)
    return generator


def test_image_prompt(alt_text_generator: AltTextGenerator):
    assert TINY_IMAGE.exists(), f"{TINY_IMAGE.absolute().as_posix()} does not exist"
    response = alt_text_generator.generate(
        TINY_IMAGE.absolute().as_posix(), "Describe the image"
    )
    assert isinstance(response, str)
    assert len(response) > 1
