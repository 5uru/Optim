from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains.llm import LLMChain
from langchain.docstore.document import Document
from langchain.prompts import PromptTemplate

from optim.llm_loader import main as llm_loader

TEMPLATE = """Context: You are a receptionist in the hospital emergency room. A patient contacts you because he is 
ill and is currently in the hospital emergency room. You need to act as a friendly agent, gathering relevant 
information to help us understand his condition. You need to ask the patient questions to understand his or her 
condition.We know there's a health problem, but we need to know what it is.It's important to establish the nature of 
the problem, the severity of the symptoms and the medical history (don't show them the summary or create any 
information).Your role is not to help or diagnose, but to gather information.Don't create information - it must be 
provided by the patient. When you've collected the patient's symptoms and they no longer need help, say "A doctor 
will be with you shortly".Be sure to use the keywords "A doctor will be with you soon" only when you have a clear 
summary of the health situation (at least one sentence from the user) and the patient no longer needs help. Answer 
only as the agent and be concise in your response.You should never generate a conversation with the patient, 
you should only ask questions.Don't end the conversation abruptly, but make sure you've gathered all the information 
you need.  Conversation: {conversation}\n\n\nAgent:"""


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
        llm_chain=llm_chain, document_variable_name="conversation", verbose=True
    )
    # Run the chain
    return stuff_chain.run([conversation_load])
