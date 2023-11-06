# Import necessary  libraries

import uuid

import streamlit as st

from optim.chat_manager import main as chat_manager

st.set_page_config(page_title=" Optim Assistant", layout="wide")


@st.cache_data
# save the chat name in the cache
def get_constants() -> dict:
    """
    Generates a random UUID and convert it to a string
    :return: dictionary with the chat name as a key and the UUID as a value.
    :rtype: dict[str, str]
    :Example:
    >>> get_constants()
    {'CHAT_NAME': 'a7a8e0d3-3e8d-4f3c-8a1d-9d9e8d9e8d9e'}
    """
    return {"CHAT_NAME": str(uuid.uuid4())}


constants = get_constants()

st.title("💬 Chatbot")
# session state for storing messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Agent", "content": "How can I help you?"}]

# display the messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# add a chat input
if user_message := st.chat_input():
    # add the user message to the session state
    st.session_state.messages.append({"role": "Patient", "content": user_message})
    st.chat_message("user").write(user_message)
    conversation = " "  # initialize the conversation string
    for msg in st.session_state.messages:
        # add the role and content of each message to the conversation string
        conversation += "\n\n\n" + msg["role"] + ": " + msg["content"]
    # get the response from the chat manager
    response = chat_manager(conversation)
    st.session_state.messages.append({"role": "Agent", "content": response})
    st.chat_message("assistant").write(response)
    # save the conversation in a file
    with open(f"Chat-Data/{constants['CHAT_NAME']}.txt", "w") as f:
        f.write(conversation)
