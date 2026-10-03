from pathlib import Path

from loaders.pdf_loader import PDFLoader
from loaders.docx_loader import DOCXLoader
from loaders.txt_loader import TXTLoader
from loaders.image_loader import ImageLoader


class LoaderFactory:

    @staticmethod
    def get_loader(file_path: str):

        extension = Path(file_path).suffix.lower()

        if extension == ".pdf":
            return PDFLoader(file_path)

        elif extension == ".docx":
            return DOCXLoader(file_path)

        elif extension == ".txt":
            return TXTLoader(file_path)

        elif extension in [".png", ".jpg", ".jpeg"]:
            return ImageLoader(file_path)

        else:
            raise ValueError(f"Unsupported file type: {extension}")