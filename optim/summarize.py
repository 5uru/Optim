from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

from llm_loader import main as llm_loader

SUMMARY_PROMPT = """
    Please provide a summary of the conversation below:\n\n###\n\n{conversation}\nThe summary is as follows: [MASK].
    """


def main(conversation: str):
    """
    The function processes a conversation by loading an LLM model, creating a prompt template, and running
    the conversation through a chain of language processing modules to generate a concise summary of the conversation.
    :param conversation: The conversation data to process.
    :type conversation: str
    :return: The processed result of the conversation.
    :rtype: str
    """
    llm = llm_loader()
    prompt = PromptTemplate.from_template(template=SUMMARY_PROMPT)
    # Conversation loader
    conversation_load = Document(page_content=conversation)
    # Define LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain, document_variable_name="conversation", verbose=True
    )
    return stuff_chain.run([conversation_load])
