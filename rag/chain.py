from langchain_openrouter import ChatOpenRouter
from langchain_core.output_parsers import StrOutputParser
from settings import LLM_MODEL
from prompts.medical_prompt import MEDICAL_PROMPT


# OpenRouter LLM
openrouter_llm = ChatOpenRouter(
    model=LLM_MODEL,
    temperature=0.2,
)


class MedicalChain:

    def __init__(self):
        self.chain = (
            MEDICAL_PROMPT
            | openrouter_llm
            | StrOutputParser()
        )

    def invoke(self, context, question):
        return self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )