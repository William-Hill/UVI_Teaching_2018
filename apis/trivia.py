import requests
import time
import json

response = requests.get("https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=multiple")
print ("response.json:", response.json()['results'][0]['question'])
