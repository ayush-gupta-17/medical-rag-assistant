from langchain_core.documents import Document


class ContextFormatter:

    @staticmethod
    def format(documents: list[Document]) -> str:
        """
        Convert retrieved documents into a single context string.
        """

        return "\n\n".join(
            doc.page_content
            for doc in documents
        )

    @staticmethod
    def citations(documents: list[Document]):

        citations = []

        for doc in documents:

            source = doc.metadata.get("source", "Unknown")

            page = doc.metadata.get("page", "?")

            citation = f"{source} (Page {page})"

            if citation not in citations:
                citations.append(citation)

        return citations