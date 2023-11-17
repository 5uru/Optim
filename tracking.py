# Import necessary  libraries
from datetime import datetime

import hydralit_components as hc
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
from streamlit_extras.stylable_container import stylable_container

from optim.evaluate import main as evaluate

import json

import os

st.set_page_config(page_title=" Optim Tracking", layout="wide")


@st.cache_data
def get_data():
    """
    Gets the data by evaluating and updating the data.json file. Returns the patient number, critic patient number,
    and the patient data.
    :return:  Tuple[int, int, dict]: A tuple containing the patient number, critic patient number, and the patient data.
    """
    # Update data.json
    data_ = evaluate()
    #  Get patient number and critic patient numbers
    patient_number = len(data_['patient_list'])
    critic_number = sum(bool(value["symptoms_alerte"])
                        for symptom, value in data_["patients"].items())
    return patient_number, critic_number, data_["patients"]


patient_number_total, critic_patient_number, patients_data = get_data()


def delete_patient(patient_number: str):
    """
    Deletes a patient from the data.json file.
    :param patient_number: (str) The patient number to delete.
    :return: None
    """
    with open("data.json", "r") as f:
        data_news = json.load(f)
    data_news["patient_list"].remove(patient_number)
    data_news["patients"].pop(patient_number)
    with open("data.json", "w") as f:
        json.dump(data_news, f, indent=4)
    # delete the patient's data from f"conversations/{patient_number}.json"
    try:
        os.remove(f"conversations/{patient_number}.json")
        st.success("Patient deleted successfully")
    except FileNotFoundError:
        st.error("Patient not found")
    return None


def card(patient_: str, score: str, time_: int, summary: str, conversation: json):
    """
    Creates a card for displaying patient information, score, time, summary, and conversation details.
    :param patient_: (str) The patient number.
    :param score: (str) The score value.
    :param time_: (int) The time value.
    :param summary: (str) The summary of the conversation.
    :param conversation: (json) The conversation details.
    :return: None
    """
    with stylable_container(
            key="container_with_border",
            css_styles="""
                    {
                        border: 1px solid rgba(49, 51, 63, 0.2);
                        border-radius: 0.5rem;
                        padding: calc(1em - 1px);
                    }
                    """,
    ):
        col_score, col_time = st.columns(2)
        col_score.metric(label=":red[Score]", value=score)
        col_time.metric(label=":red[Time]", value=time_)
        st.text(f"Patient Number: {patient_}")
        st.text("Summary:")
        st.markdown(summary)
        with st.expander("Details"):
            st.json(conversation)
        if st.button("Delete", key=patient_):
            delete_patient(patient_)
            st.rerun()


with st.spinner('Wait for it...'):
    col1, col2 = st.columns(2)
    theme_bad = {'bgcolor': '#FFF0F0', 'title_color': 'red', 'content_color': 'red', 'icon_color': 'red',
                 'icon': 'fa fa-times-circle'}
    with col1:
        hc.info_card(title='Patient Number', content=f"{patient_number_total}", sentiment='good', )
    with col2:
        hc.info_card(title='Critic Patient Number', content=f"{critic_patient_number}", theme_override=theme_bad)
    add_vertical_space(1)
    _, col = st.columns([8, 1])
    with col:
        on = st.toggle("Sort by Score", True)
    add_vertical_space(1)
    icon_row = row(3)  # number of rows
    if on:
        # Sort by patient by score
        patients_data = sorted(patients_data.items(), key=lambda x: x[1]["score"], reverse=True)
    else:
        # Sort by patient by time
        patients_data = sorted(patients_data.items(), key=lambda x: x[1]["date"], reverse=False)
    for patient, data in patients_data:
        # calculate time
        time = (datetime.now() - datetime.strptime(data["date"], "%Y-%m-%d %H:%M:%S")).total_seconds()
        time = round(time / 60)  # round to minutes
        with icon_row.container():
            card(patient, data["score"], time, data["summary"], json.dumps(data, indent=4))
