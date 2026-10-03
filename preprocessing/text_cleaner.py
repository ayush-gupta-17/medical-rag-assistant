import re

from langchain_core.documents import Document


class TextCleaner:
    """
    Cleans extracted text while preserving metadata.
    """

    @staticmethod
    def clean(documents: list[Document]) -> list[Document]:

        cleaned_documents = []

        for doc in documents:

            text = doc.page_content

            # Remove multiple spaces
            text = re.sub(r"\s+", " ", text)

            # Remove multiple blank lines
            text = re.sub(r"\n+", "\n", text)

            # Remove leading/trailing whitespace
            text = text.strip()

            cleaned_documents.append(
                Document(
                    page_content=text,
                    metadata=doc.metadata
                )
            )

        return cleaned_documents