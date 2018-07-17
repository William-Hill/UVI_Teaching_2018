import requests

def get_number_fact():
    while True:
        try:
            num = int(input("What number do you want a fact about? "))
        except ValueError:
            print("That's not an int! Please enter a valid number.")
        else:
            response = requests.get("http://numbersapi.com/{}".format(num))
            print(response.text)

            another_one = input("Would you like another number fact? ")
            if another_one.lower() in ["yes", "y"]:
                continue
            elif another_one.lower() in ["no", "n"]:
                break
            else:
                print("Invalid input so I'm going to tell you another fact anyway")
                continue

def main():
    get_number_fact()

main()
