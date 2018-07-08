import requests
import json

# response = requests.get("http://pokeapi.co/api/v2/pokemon/charizard")
response = requests.get("https://api.pokemontcg.io/v1/cards?name=pikachu&pageSize=2")
# text = response.json()
text = response.text
parsed = json.loads(text)
print json.dumps(parsed, indent=4, sort_keys=True)
# print "text type:", type(text)
# print "text.forms:", text["forms"]
# print "forms type:", type(text["forms"])
# print "response text:", response.text
