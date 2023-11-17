# Optim: Emergency Department Symptom Classifier


## Overview
Optim is an innovative project developed for the **IndabaX Bénin 2023 Hackathon** aimed at enhancing the efficiency of emergency departments (EDs). Utilizing a ChatGPT-powered chat interface, Optim classifies patients based on the severity of their symptoms, enabling quicker and more accurate triage decisions.

## How It Works

* **Input:** Users enter symptoms using natural language. They can describe their condition in their own words, just like talking to a doctor.
* **Processing:** The ChatGPT model interprets the input, identifying key symptoms and their implied severity.
* **Output:** The system categorizes the case into a severity level (e.g., High, Medium, Low Urgency)

## Advantages
**Accessibility:** User-friendly for people of all ages and tech-heaviness.
**Efficiency:** Speeds up the triage process by providing instant preliminary assessments.
**Accuracy:** Utilizes the extensive knowledge base of ChatGPT to understand a wide range of medical symptoms and conditions.

## Datasets : https://www.kaggle.com/datasets/itachi9604/disease-symptom-description-dataset?select=Symptom-severity.csv

## Technology Stack
* **ChatGPT:** Powered by OpenAI's ChatGPT for natural language processing.
* **Langchain:** A natural language processing library for Python.
* **Streamlit:** A Python library for building interactive web apps.

## Installation
Provide step-by-step instructions on how to set up and run Optim in a local development environment.
* **Clone the repository:** `git clone https://github.com/JoSuru/Optim.git`
* **Install dependencies:** `pip install -r requirements.txt`
* **Environment variables:**
    * `export OPENAI_API_KEY=<your key>`
    * `export OPENAI_ORG=<your org id>`

## Usage
* **Run the app:** `streamlit run optim.py` (for Patient chat)
* **Run the app:** `streamlit run tracking.py` (for Patient tracking)

## Screenshots
## Patient Chat
![Chat](Capture%20d%E2%80%99%C3%A9cran%202023-11-17%20%C3%A0%2021.10.23.png)
## Patient Tracking
![Tracking](Capture%20d%E2%80%99%C3%A9cran%202023-11-17%20%C3%A0%2021.14.56.png)