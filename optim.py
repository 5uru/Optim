# Import necessary  libraries

import glob
import json
from datetime import datetime

import streamlit as st

from optim.chat_manager import main as chat_manager

st.set_page_config(page_title=" Optim Assistant", layout="wide")


@st.cache_data
# save the chat name in the cache
def patient_position() -> dict:
    """
    This code defines a function named patient_position that returns a dictionary with a single key-value pair. The
    function finds the maximum file name in a directory, increments it by 1, and returns it as the value for the key
    "CHAT_NAME" in the dictionary.
    :return: a dictionary with a single key-value pair
    :rtype: dict[str, str]
    :Example:
    >>> patient_position()
    {'CHAT_NAME': '1'}
    """
    # get all the json files in the conversations directory
    json_files = glob.glob('conversations/*.json')
    # delete ".json" and "conversations/" from the file name
    json_files = [file.replace(".json", "").replace("conversations/", "") for file in json_files]
    json_files = [int(file) for file in json_files]  # convert the file name to an integer
    try:
        max_names = max(json_files)  # get the maximum file name
    except ValueError:
        max_names = 0  # if the directory is empty, set max_names to 0
    file_name = str(max_names + 1)  # increment the file name by 1
    return {"CHAT_NAME": file_name}


# get the chat name from the cache
constants = patient_position()

st.title("💬 Chatbot")
# write the patient number position
st.text("Patient Number: " + constants["CHAT_NAME"])
# session state for storing messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Agent", "content": "Hello"}]

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
    # save the conversation in a file json file
    with open(f"conversations/{constants['CHAT_NAME']}.json", "w") as f:
        data = {"messages": conversation, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        json.dump(data, f)
