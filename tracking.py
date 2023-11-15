# Import necessary  libraries

import hydralit_components as hc
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row
from streamlit_extras.stylable_container import stylable_container

from optim.evaluate import main as evaluate

import json

st.set_page_config(page_title=" Optim Tracking", layout="wide")


@st.cache_data
def get_data():
    # Update data.json
    evaluate()
    # Open data.json
    with open('data.json') as f:
        data = json.load(f)
    #  Get patient number and critic patient numbers
    patient_number = len(data['patient_list'])
    critic_number = sum(bool(value["symptoms_alerte"])
                        for symptom, value in data["patients"].items())
    return patient_number, critic_number


patient_number_total, critic_patient_number = get_data()


def card():
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
        col_score.metric(label=":red[Score]", value=5000)
        col_time.metric(label=":red[Time]", value=5000)
        st.text("Patient Number: 1")
        st.text("Summary:")
        st.markdown(
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae nibh ac nisl aliquam lacinia.")
        with st.expander("Details"):
            st.markdown(
                "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vitae nibh ac nisl aliquam lacinia.")


with st.spinner('Wait for it...'):
    col1, col2 = st.columns(2)
    theme_bad = {'bgcolor': '#FFF0F0', 'title_color': 'red', 'content_color': 'red', 'icon_color': 'red',
                 'icon': 'fa fa-times-circle'}
    with col1:
        hc.info_card(title='Patient Number', content='1200', sentiment='good', )
    with col2:
        hc.info_card(title='Critic Patient Number', content='30', theme_override=theme_bad)
    add_vertical_space(1)
    _, col = st.columns([8, 1])
    with col:
        on = st.toggle('Activate feature')
    add_vertical_space(1)
    icon_row = row(3)  # number of rows
    if on:

        with icon_row.container():
            card()
    else:
        with icon_row.container():
            card()
