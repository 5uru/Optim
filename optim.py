# Import necessary  libraries

import streamlit as st

from optim.chat_manager import main as chat_manager

st.set_page_config(page_title=" Optim Assistant", layout="wide")


st.title("💬 Chatbot")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Agent", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "Patient", "content": prompt})
    st.chat_message("user").write(prompt)
    conversation = " "
    for msg in st.session_state.messages:
        conversation += "\n\n\n" + msg["role"] + ": " + msg["content"]
    with open("output.txt", "w") as f:
        f.write(conversation)
    response = chat_manager(conversation)
    st.session_state.messages.append({"role": "Agent", "content": response})
    st.chat_message("assistant").write(response)
