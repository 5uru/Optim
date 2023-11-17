import glob
import json

from optim.extraction import main as extract
from optim.summarize import main as summarize


def update_chat(patient: str):
    """
    Updates the chat conversation for a given patient.

    Opens the patient data file and loads the conversation. Checks if the conversation dictionary contains the keys
    "summary", "score", and "symptoms". If any of these keys are missing, performs the corresponding calculations or
    extraction and updates the conversation dictionary accordingly. Finally, saves the updated conversation back to the
    patient data file.

    :param:
        patient (str): The path to the patient data file.

    :return:
        dict: The updated conversation dictionary.
    """
    # Open the patient data
    with open(patient, "r") as f:
        conversation = json.load(f)
    conversation["summary"] = summarize(
        conversation["messages"]
    )  # Summarize the conversation
    conversation["symptoms"] = extract(
        conversation["summary"]
    )  # Extract symptoms from the conversation
    patient_score = score(
        conversation["symptoms"]
    )  # Calculate the score and symptoms_alerte
    conversation["score"] = patient_score[
        "score"
    ]  # Calculate the score of the conversation
    conversation["symptoms_alerte"] = patient_score["symptoms_alerte"]  # Calculate the
    # symptoms_alerte of the conversation
    # Save the conversation in the json file
    with open(patient, "w") as f:
        json.dump(conversation, f)
    return conversation


def score(symptoms: dict) -> dict:
    """
    Calculates the score and symptoms alert for a given set of symptoms.

    Opens the "score.json" file and loads the scores. Iterates through the symptoms and their corresponding values,
    calculating the total score based on the scores' dictionary. Determines if any symptom has a score greater than
    4, setting the symptoms_alerte flag accordingly. Returns a dictionary containing the calculated score and
    symptoms_alerte.

    :param:
        symptoms (dict): A dictionary of symptoms and their values.

    :return:
        dict: A dictionary containing the calculated score and symptoms_alerte.
    """

    # Open the score.json file
    with open("./score.json", "r") as f:
        scores = json.load(f)
    scores_total = 0  # The total score
    symptoms_alerte = (
        False
    )  # if the score of a symptom is greater than 5 then symptoms_alerte is True
    # Loop through the symptoms and their values
    for symptom, value in symptoms.items():
        # Check if the symptom is in the score dictionary
        if value:
            try:
                # Add the score to the total score
                scores_total += scores[symptom]
                # Check if the score is greater than 5
                if scores[symptom] > 5:
                    symptoms_alerte = True
            except KeyError:  # If the symptom is not in the score dictionary
                print(f"Symptom {symptom} not found in score.json")
    # Return the score and symptoms_alerte
    return {"score": scores_total, "symptoms_alerte": symptoms_alerte}


def main():
    """
    Runs the main evaluation process.

    Retrieves all JSON files in the "conversations" directory and extracts the patient names. Opens the "data.json" file
    and loads the data. Checks if each patient in the patient list is already present in the data. If not, evaluates the
    corresponding conversation using the "update_chat" function and adds it to the data dictionary. Finally, saves the
    updated data dictionary back to the "data.json" file and returns it.

    :return:
        dict: The updated data dictionary.
    """

    # get all the json files in the conversations directory
    json_files = glob.glob("./conversations/*.json")
    # delete ".json" and "conversations/" from the file name
    patient_list = [
        file.replace(".json", "").replace("./conversations/", "") for file in json_files
    ]
    # open "data.json" for reading
    with open("./data.json", "r") as f:
        data = json.load(f)
    # check if the patient list in patient_list is not in the data patient list
    for patient in patient_list:
        if patient not in data["patient_list"]:
            # evaluate the conversation
            conversation = update_chat(f"./conversations/{patient}.json")
            # add the conversation to the data dictionary
            data["patients"][patient] = conversation
            # add the patient to the patient list
            data["patient_list"].append(patient)
    # save the data dictionary in the json file
    with open("./data.json", "w") as f:
        json.dump(data, f)
    # return the data dictionary
    return data
