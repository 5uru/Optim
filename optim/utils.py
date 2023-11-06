from hydra import initialize, compose
from langchain.embeddings import HuggingFaceEmbeddings


def embedding_model():
    """
    This code defines a function named embedding_model that initializes and returns a HuggingFaceEmbeddings model for
    text embeddings. :return:
    """
    with initialize(config_path="../conf", version_base="1.3"):
        cfg = compose(config_name="config.yaml")

    # embeddings model
    model_name = cfg.embeddings.model_namÒe
    model_kwargs = {"device": cfg.embeddings.device}
    encode_kwargs = {"normalize_embeddings": cfg.embeddings.normalize_embeddings}
    # return HuggingFaces embeddings model
    return HuggingFaceEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs,
    )
