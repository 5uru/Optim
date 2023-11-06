from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

from optim.llm_loader import main as llm_loader

# open the template file
with open("Data/chat_prompt.txt", "r") as f:
    TEMPLATE = f.read()


def main(chat_history: str) -> str:
    """
    The main function is responsible for running a chain of processes to generate a response based on a given chat
    history.
    :param chat_history: The chat history to generate a response.
    :type chat_history: str
    :return: The generated response based on the given chat history.
    :rtype: str
    """
    # Load LLM
    llm = llm_loader()
    # Prompt template for messages
    prompt = PromptTemplate.from_template(template=TEMPLATE)
    # Conversation loader
    conversation_load = Document(page_content=chat_history)
    # Define LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)
    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain, document_variable_name="conversation", verbose=False
    )
    # Run the chain
    return stuff_chain.run([conversation_load])
