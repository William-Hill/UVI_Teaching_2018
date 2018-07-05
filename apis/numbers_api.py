import requests

number = raw_input("What number do you want a fact about? ")
response = requests.get("http://numbersapi.com/{}".format(number))
print "response:", response
print "response text:", response.text
