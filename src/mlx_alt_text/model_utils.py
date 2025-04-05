from huggingface_hub import snapshot_download
from huggingface_hub.utils.tqdm import disable_progress_bars


def download_model(
    model_name: str, verbose: bool = False, progress_bars: bool = True
) -> str:
    """Download a model for use with AltTextGenerator."""

    if verbose:
        print(f"Downloading model: {model_name}...")

    if not progress_bars:
        disable_progress_bars()

    model_path = snapshot_download(
        repo_id=model_name,
        allow_patterns=[
            "*.json",
            "*.safetensors",
            "*.py",
            "tokenizer.model",
            "*.tiktoken",
            "*.txt",
        ],
    )

    if verbose:
        print(f"Model downloaded to: {model_path}")

    return model_path
