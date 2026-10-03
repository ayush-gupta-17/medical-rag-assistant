from langchain_core.documents import Document


class MetadataProcessor:

    @staticmethod
    def enrich(documents: list[Document]):

        for index, doc in enumerate(documents):

            doc.metadata["chunk_id"] = index + 1

        return documents