import requests

name = input("Enter a name to guess its gender: ")
response = requests.get("https://api.genderize.io/?name={}".format(name))

print("response:", response.json())
