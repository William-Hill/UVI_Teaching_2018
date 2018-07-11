import requests
import time
import json

while True:
    response = requests.get("https://08ad1pao69.execute-api.us-east-1.amazonaws.com/dev/random_joke")
    print "joke:", response.json()["setup"]
    # print "joke type:", type(response.content)
    time.sleep(2.0)
    print response.json()["punchline"]

    another_one = raw_input("Would you like to hear another joke? ")
    if another_one.lower() in ["yes", "y"]:
        continue
    elif another_one.lower() in ["no", "n"]:
        break
    else:
        print "Invalid input so I'm going to tell you another joke anyway"
        continue
