from rag.chain import MedicalChain
from rag.formatter import ContextFormatter
from vectorstore.retriever import MedicalRetriever


class MedicalChatbot:

    def __init__(self):

        self.retriever = MedicalRetriever()

        self.chain = MedicalChain()

    def ask(self, question):

        documents = self.retriever.retrieve(question)

        context = ContextFormatter.format(documents)

        answer = self.chain.invoke(
            context=context,
            question=question
        )

        citations = ContextFormatter.citations(documents)

        return {
            "answer": answer,
            "citations": citations
        }