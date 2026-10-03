from pathlib import Path
from langchain_chroma import Chroma
from settings import CHROMA_DB_DIR
from embeddings.embedding_model import EmbeddingModel


class ChromaStore:
    """
    Handles all interactions with ChromaDB.
    """

    COLLECTION_NAME = "medical_reports"

    def __init__(self):
        self.embedding_function = EmbeddingModel().get_embeddings()

        self.vectorstore = Chroma(
            collection_name=self.COLLECTION_NAME,
            persist_directory=CHROMA_DB_DIR,
            embedding_function=self.embedding_function,
        )

    def add_documents(self, documents):
        """
        Add documents to the vector database.
        """
        self.vectorstore.add_documents(documents)

    def get_vectorstore(self):
        """
        Return the Chroma instance.
        """
        return self.vectorstore

    @classmethod
    def reset_database(cls):
        """
        Safely clears all documents from the vector database without breaking collection handles.
        """
        try:
            store = cls()
            # Fetch all document IDs currently in the collection
            existing_docs = store.vectorstore.get()
            if existing_docs and existing_docs.get("ids"):
                # Delete documents by ID rather than deleting the whole collection
                store.vectorstore.delete(ids=existing_docs["ids"])
                print("All documents cleared from collection successfully.")
            else:
                print("Vector store is already empty.")
        except Exception as e:
            print(f"Error resetting database: {e}")