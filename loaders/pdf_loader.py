import fitz
from pathlib import Path

from langchain_core.documents import Document


class PDFLoader:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):

        documents = []

        pdf = fitz.open(self.file_path)

        for page_number, page in enumerate(pdf):

            text = page.get_text().strip()

            if not text:
                continue

            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": Path(self.file_path).name,
                        "page": page_number + 1,
                        "file_type": "pdf"
                    }
                )
            )

        pdf.close()

        return documents