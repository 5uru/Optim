# open conversations/11.json
import json

from optim.extraction import main as extract

with open("./conversations/11.json", "r") as f:
    conversation = json.load(f)

print(extract(conversation["messages"]))
