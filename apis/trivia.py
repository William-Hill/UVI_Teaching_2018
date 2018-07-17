import requests
import time
import json

import html.parser as htmlparser

def get_trivia_questions():
    # response = requests.get("https://opentdb.com/api.php?amount=3&category=15&difficulty=easy&type=multiple")
    response = requests.get("https://opentdb.com/api.php?amount=5&category=32&type=multiple")
    print("response:", response.json())
    question_info = response.json()['results']
    number_of_questions = len(question_info)
    print("number_of_questions:", number_of_questions)
    parser = htmlparser.HTMLParser()
    score = 0
    for question_number in range(number_of_questions):
        question = parser.unescape(question_info[question_number]['question'])
        user_answer = input(question)
        api_answer = question_info[question_number]['correct_answer'].lower()
        if user_answer.lower() == api_answer:
            print("You are correct!")
            score +=1
        else:
            print("WRONG!!!!")
            print("The correct answer is:", api_answer)

    print("Your score is ", score)

def main():
    get_trivia_questions()

main()
