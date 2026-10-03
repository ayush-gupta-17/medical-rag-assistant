import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ==========================
# API Keys
# ==========================
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# ==========================
# Project Directories
# ==========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
CHROMA_DB_DIR = os.path.join(BASE_DIR, "chroma_db")

# ==========================
# Chunking Configuration
# ==========================
CHUNK_SIZE = 700
CHUNK_OVERLAP = 150

# ==========================
# Embedding Model
# ==========================
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# ==========================
# LLM Configuration
# ==========================
LLM_MODEL = "openrouter/free"

# ==========================
# Retriever Configuration
# ==========================
TOP_K = 5

# ==========================
# Supported File Types
# ==========================
SUPPORTED_EXTENSIONS = [
    ".pdf",
    ".docx",
    ".txt",
    ".png",
    ".jpg",
    ".jpeg",
]