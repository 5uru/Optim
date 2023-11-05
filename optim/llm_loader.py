from hydra import initialize, compose
from langchain.llms import Ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler


def main():
    with initialize(config_path="../conf", version_base="1.3"):
        cfg = compose(config_name="config.yaml")
    if cfg.llm.name == "ollama":
        llm = Ollama(
            model=cfg.llm.model_name,
            verbose=False,
            callback_manager=CallbackManager([StreamingStdOutCallbackHandler()]),
        )
        return llm
