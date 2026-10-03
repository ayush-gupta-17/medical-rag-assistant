from pathlib import Path

from langchain_core.documents import Document


class TXTLoader:

    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):

        with open(self.file_path, "r", encoding="utf-8") as file:
            text = file.read()

        return [
            Document(
                page_content=text,
                metadata={
                    "source": Path(self.file_path).name,
                    "page": 1,
                    "file_type": "txt"
                }
            )
        ]