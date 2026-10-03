import os
import sys
import tempfile
import streamlit as st

# Ensure root directory is in python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rag.ingestion import DocumentIngestion
from rag.chatbot import MedicalChatbot

# Page Configuration
st.set_page_config(
    page_title="MediAssist AI",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 MediAssist AI")
st.subheader("Intelligent Medical RAG Assistant")

# Initialize Chatbot and state tracking in session_state
if "chatbot" not in st.session_state:
    st.session_state.chatbot = MedicalChatbot()

if "processed_file" not in st.session_state:
    st.session_state.processed_file = None

if "chunks_count" not in st.session_state:
    st.session_state.chunks_count = 0

# File Upload Widget
uploaded_file = st.file_uploader(
    "Upload a Medical Report",
    type=["pdf", "docx", "txt", "png", "jpg", "jpeg"]
)

if uploaded_file:
    # Trigger ingestion only when a new file is uploaded
    if st.session_state.processed_file != uploaded_file.name:
        
        # 1. Safely handle temp file for Windows OS
        file_ext = os.path.splitext(uploaded_file.name)[1]
        with tempfile.NamedTemporaryFile(delete=False, suffix=file_ext) as tmp:
            tmp.write(uploaded_file.read())
            file_path = tmp.name

        try:
            with st.spinner("Processing report and updating vector database..."):
                # 2. Reset DB & Ingest
                chunks = DocumentIngestion().ingest(file_path)
                st.session_state.chunks_count = chunks
                st.session_state.processed_file = uploaded_file.name
                
                # 3. Refresh chatbot to re-bind retriever to new Chroma state
                st.session_state.chatbot = MedicalChatbot()
        finally:
            # Clean up temp file safely from disk
            if os.path.exists(file_path):
                os.unlink(file_path)

    st.success(
        f"Report processed successfully! ({st.session_state.chunks_count} chunks indexed)"
    )

    # Question & Answer Section
    question = st.text_input("Ask a question about your medical report")

    if question.strip():
        with st.spinner("Generating answer..."):
            response = st.session_state.chatbot.ask(question)

        st.markdown("## Answer")
        st.write(response["answer"])

        # Display source citations if returned
        if response.get("citations"):
            st.markdown("## Sources")
            for citation in response["citations"]:
                st.write(f"- {citation}")