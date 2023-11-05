from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

from optim.llm_loader import main as llm_loader

with open("Data/chat_prompt.txt", "r") as f:
    TEMPLATE = f.read()


def main(chat_history):
    llm = llm_loader()

    prompt = PromptTemplate.from_template(template=TEMPLATE)
    # Conversation loader
    conversation_load = Document(page_content=chat_history)
    # Define LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain, document_variable_name="conversation", verbose=False
    )
    return stuff_chain.run([conversation_load])
