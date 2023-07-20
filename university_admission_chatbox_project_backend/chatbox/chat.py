import random
import requests
import json
import torch

from chatbox.deep_learning_model import NeuralNet
from chatbox.nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('chatbox/intents.json', 'r') as f:
    intents = json.load(f)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data["all_words"]
tags = data["tags"]
model_state = data["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Unichatty"

api_url = "https://api.data.gov/ed/collegescorecard/v1/schools/?school.operating=1&2020.student.size__range=1..&school.degrees_awarded.predominant__range=1..3&school.degrees_awarded.highest__range=2..4&api_key=I5gr1WgKH4UfV87xbbRK6vcwqlKrq4YPPL1C7eTx"

def fetch_university_info():
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            return data['results']
        else:
            print(f"Failed to fetch university data. Status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"An error occurred while fetching university data: {e}")
    
    return []

def get_admission_requirements(university_data, sentence):
    for result in university_data:
        school_data = result.get('2020', {}).get('school', {})
        school_data = school_data.get('name').split()
        for name in school_data:
            if name in sentence:
                admissions_data = result.get('2020', {}).get('admissions', {})
                admission_requirements = {
                    'test_requirements': admissions_data.get('test_requiremetns'),
                    'admission_rate': admissions_data.get('admission_rate'),
                    'act_scores': admissions_data.get('act_scores'),
                    'sat_scores': admissions_data.get('sat_scores')
                }
                response = f"{admission_requirements}"
                return response

def search_universities(university_data):
    for result in university_data:
        school_data = result.get('2020', {}).get('school', {})
        school_name = school_data.get('name')
        if school_name:
            all_schools.append(school_name)
        response = f"{all_schools}"
    return response

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    
    
    university_data = fetch_university_info()
    all_schools = []
    
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                if intent["tag"] == "search_universities":
                    response = search_universities(university_data)

                elif intent["tag"] == "admission_requirements":
                    response = get_admission_requirements(university_data, sentence)

    return "I do not understand..."



print("Let's chat! (type 'quit' to exit)")
while True:
    # sentence = "do you use credit cards?"
    sentence = input("You: ")
    if sentence == "quit":
        break

    resp = get_response(sentence)
    print(resp)