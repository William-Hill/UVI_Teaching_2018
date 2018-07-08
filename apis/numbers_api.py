import requests

while True:
    try:
        num = int(raw_input("What number do you want a fact about? "))
    except ValueError:
        print "That's not an int! Please enter a valid number."
    else:
        break
response = requests.get("http://numbersapi.com/{}".format(num))
print "response text:", response.text
