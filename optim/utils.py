from hydra import initialize, compose
from langchain.embeddings import HuggingFaceEmbeddings


def embedding_model():
    with initialize(config_path="../conf", version_base="1.3"):
        cfg = compose(config_name="config.yaml")

    # embeddings model
    model_name = cfg.embeddings.model_namÒe
    model_kwargs = {"device": cfg.embeddings.device}
    encode_kwargs = {"normalize_embeddings": cfg.embeddings.normalize_embeddings}
    hf_embeddings = HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
    )
    return hf_embeddings


def get_chat_history(inputs) -> str:
    res = []
    for human, ai in inputs:
        res.append(f"Customer:{human}\nAgent:{ai}")
    return "\n".join(res)
