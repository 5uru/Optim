from typing import Any, List, Dict, Mapping, Optional

from hydra import initialize, compose
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from omegaconf import OmegaConf
from pydantic import Field

# load the config
with initialize(config_path="../conf", version_base="1.3"):
    cfg = compose(config_name="config.yaml")
    OmegaConf.resolve(cfg)


class BananaDev(LLM):
    """
    The 'BananaDev' class is a custom language model manager (LLM) that allows users to interact with a language model
    hosted on the Banana platform. It provides a method for calling the model with a given prompt and returning the
    generated text. The class also handles errors related to importing the 'banana-dev' package and parsing the response
    from the model.
    """
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)

    # configuration parameters
    api_key = cfg.llms.api_key
    model_url = cfg.llms.model_url

    @property
    def _llm_type(self) -> str:
        return "custom"

    def _call(
            self,
            prompt: str,
            stop: Optional[List[str]] = None,
            run_manager: Optional[CallbackManagerForLLMRun] = None,
            **kwargs: Any,
    ) -> str:
        try:
            import banana_dev as client
        except ImportError as e:
            raise ImportError(
                "Could not import banana-dev python package. "
                "Please install it with `pip install banana-dev`."
            ) from e
        params = self.model_kwargs or {}
        params = {**params, **kwargs}
        model_inputs = {
            # a json specific to your model.
            "prompt": prompt,
            **params,
        }
        # Create a reference to your model on Banana
        my_model = client.Client(
            api_key=self.api_key,
            url=self.model_url,
        )
        response, _ = my_model.call("/", model_inputs)
        try:
            text = response["outputs"]["sequence"]
        except (KeyError, TypeError) as e:
            returned = response["outputs"]
            raise ValueError(
                "Response should be of schema: {'output': 'text'}."
                f"\nResponse was: {returned}"
                "\nTo fix this:"
                "\n- fork the source repo of the Banana model"
                "\n- modify app.py to return the above schema"
                "\n- deploy that as a custom repo"
            ) from e
        if stop is not None:
            # I believe this is required since the stop tokens
            # are not enforced by the model parameters
            text = enforce_stop_tokens(text, stop)
        return text

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {}