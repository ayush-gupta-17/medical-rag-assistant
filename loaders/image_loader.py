from pathlib import Path
import easyocr

from langchain_core.documents import Document


class ImageLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.reader = easyocr.Reader(["en"])

    def load(self):

        result = self.reader.readtext(self.file_path)

        text = "\n".join(
            item[1]
            for item in result
        )

        return [
            Document(
                page_content=text,
                metadata={
                    "source": Path(self.file_path).name,
                    "page": 1,
                    "file_type": "image"
                }
            )
        ]