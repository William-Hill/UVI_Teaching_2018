import requests

response = requests.get("https://drake-bot-files.herokuapp.com/back")
open('clean_backtoback.txt', 'w').write(response.text.encode("utf-8"))

response = requests.get("https://drake-bot-files.herokuapp.com/feelings")
open('clean_inmyfeelings.txt', 'w').write(response.text.encode("utf-8"))

response = requests.get("https://drake-bot-files.herokuapp.com/hotline")
open('clean_hotlinebling.txt', 'w').write(response.text.encode("utf-8"))

response = requests.get("https://drake-bot-files.herokuapp.com/plan")
open('clean_godsplan.txt', 'w').write(response.text.encode("utf-8"))
