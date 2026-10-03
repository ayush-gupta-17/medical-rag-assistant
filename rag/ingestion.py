from loaders.loader_factory import LoaderFactory
from preprocessing.text_cleaner import TextCleaner
from preprocessing.chunking import Chunker
from preprocessing.metadata import MetadataProcessor
from vectorstore.chroma_store import ChromaStore


class DocumentIngestion:

    def __init__(self):

        self.chunker = Chunker()

    def ingest(self, file_path: str):

        # Clear old database
        ChromaStore.reset_database()

        vectorstore = ChromaStore()

        # Load
        loader = LoaderFactory.get_loader(file_path)
        documents = loader.load()

        # Clean
        documents = TextCleaner.clean(documents)

        # Chunk
        chunks = self.chunker.split(documents)

        # Metadata
        chunks = MetadataProcessor.enrich(chunks)

        # Store
        vectorstore.add_documents(chunks)

        return len(chunks)