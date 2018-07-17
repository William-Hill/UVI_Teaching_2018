import requests
import html.parser as htmlparser

response = requests.get("https://api.icndb.com/jokes/random?firstName=Tim&lastName=Kentopp")
parser = htmlparser.HTMLParser()
joke = parser.unescape(response.json()['value']['joke'])
print(joke)
