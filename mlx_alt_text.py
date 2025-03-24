from mlx import nn
from mlx_vlm import generate, load
from mlx_vlm.prompt_utils import apply_chat_template
from mlx_vlm.utils import load_config

DEFAULT_MODEL = "mlx-community/Qwen2-VL-2B-Instruct-4bit"
DEFAULT_MAX_TOKENS = 100  # TODO experiment
DEFAULT_TEMPERATURE = 0.2  # TODO experiment


class AltTextGenerator:
    """Generate alt-text using MLX=VLM"""

    def __init__(
        self,
        model_name: str = DEFAULT_MODEL,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        temperature: float = DEFAULT_TEMPERATURE,
    ):
        self.model_name = model_name
        self.max_tokens = max_tokens
        self.temperature = temperature
        self.model: None | nn.Module = None
        self.processor = None
        self.config = None

    def _load_model(self):
        """Load the model and processor if not already loaded"""
        if self.model is None:
            self.model, self.processor = load(self.model_name)
            self.config = load_config(self.model_name)
        return self.model, self.processor, self.config

    def generate(
        self, prompt: str, image: str | None = None, verbose: bool = False
    ) -> str:
        """Generate alt-text for the given image"""
        model, processor, config = self._load_model()

        formatted_prompt = apply_chat_template(processor, config, prompt)

        output = generate(
            model,
            processor,  # type: ignore
            formatted_prompt,  # type: ignore
            image=image,  # type: ignore
            verbose=verbose,
        )

        return output.strip()
