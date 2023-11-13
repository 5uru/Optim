import glob
import json

from optim.extraction import main as extract
from optim.summarize import main as summarize


def update_chat(patient: str):
    # Open the patient data
    with open(patient, "r") as f:
        conversation = json.load(f)
    # Check if the summary, score and symptoms keys are in the conversation dictionary
    if "summary" not in conversation:
        conversation["summary"] = summarize(conversation["messages"])
    elif "symptoms" not in conversation:
        conversation["symptoms"] = extract(conversation["summary"])

    # Save the conversation in the json file
    with open(patient, "w") as f:
        json.dump(conversation, f)
    return conversation


def main():
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
        if patient not in data["patients"]:
            # evaluate the conversation
            conversation = update_chat(f"./conversations/{patient}.json")
            # add the conversation to the data dictionary
            data["patients"][patient] = conversation
    # save the data dictionary in the json file
    with open("./data.json", "w") as f:
        json.dump(data, f)
    # return the data dictionary
    return data
