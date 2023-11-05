from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

from optim.llm_loader import main as llm_loader

template = """Context: You are a support worker in a hospital emergency department. A patient contacts us regarding a 
health concern. Your role as a friendly representative is to collect pertinent information to gain a full 
understanding of their condition. We are familiar with the health problem, but require clarification on the 
specifics. It is crucial to determine the problem's nature, severity of symptoms, and medical history.
  
Kindly note that no summary will be shared with the user nor any information produced. Your duty is to gather 
details, not provide aid. Do not create information, it must be provided by the customer. If the information is 
obtained, inform them that an agent will be with them shortly using the phrase "An agent". will attend to you 
shortly" only when you possess a concise overview of the issue (consisting of at least one sentence from the user), 
an order number, and an email address. Additionally, ensure that the customer is no longer in need of assistance. 
Here is the record of your conversations with the customer:\n\n {conversation}\n Agent:\n"""


def main(chat_history):
    llm = llm_loader()

    prompt = PromptTemplate.from_template(template=template)
    # Conversation loader
    conversation_load = Document(page_content=chat_history)
    # Define LLM chain
    llm_chain = LLMChain(llm=llm, prompt=prompt)

    # Define StuffDocumentsChain
    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain, document_variable_name="conversation", verbose=False
    )
    return stuff_chain.run([conversation_load])
