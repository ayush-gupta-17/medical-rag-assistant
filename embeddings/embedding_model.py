from langchain_huggingface import HuggingFaceEmbeddings

from settings import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Loads the HuggingFace embedding model.
    """

    def __init__(self):

        self.embeddings = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    def get_embeddings(self):

        return self.embeddings