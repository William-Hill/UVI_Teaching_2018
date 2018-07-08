import requests
import time
import json

response = requests.get("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke")
print "joke:", response.json()["setup"]
# print "joke type:", type(response.content)
time.sleep(1.5)
print response.json()["punchline"]
