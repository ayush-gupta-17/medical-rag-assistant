from settings import TOP_K

from vectorstore.chroma_store import ChromaStore


class MedicalRetriever:

    def __init__(self):

        self.vectorstore = ChromaStore().get_vectorstore()

    def retrieve(self, query):

        results = self.vectorstore.similarity_search(
            query=query,
            k=TOP_K
        )

        return results