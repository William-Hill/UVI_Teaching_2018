import requests
import json

# response = requests.get("http://pokeapi.co/api/v2/pokemon/charizard")
pokemon_name = raw_input("What Pokemon do you want info about? ")
response = requests.get("https://api.pokemontcg.io/v1/cards?name={}&pageSize=2".format(pokemon_name))
#TODO: if response.text["cards"] is empty; return error message
# text = response.json()
text = response.text
parsed = json.loads(text)
print json.dumps(parsed, indent=4, sort_keys=True)
# print "text type:", type(text)
# print "text.forms:", text["forms"]
# print "forms type:", type(text["forms"])
# print "response text:", response.text
