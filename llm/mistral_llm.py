from langchain_openrouter import ChatOpenRouter
from settings import LLM_MODEL

# Define the OpenRouter LLM
openrouter_llm = ChatOpenRouter(
    model=LLM_MODEL,
    temperature=0.2
)