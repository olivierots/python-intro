# create a quizzing game. make an http request to open trivial API at each round of the game
# to get a new question and present it to the user to answer.
# at the end of each round ask the user if he wants to play again. Keep playing forevr until
# the user types "quit".
# dont forget to tell if the answer is correct or not at each round and keep the user's score.

import requests
import json
import pprint # print the data (API response) in a nicer format
import random
import html

score_correct = 0
score_incorrect = 0

# my variables
url = "https://opentdb.com/api.php?amount=1"
# keep this game playing forevr until the user quit
endGame = ""

while endGame != "quit":
    r = requests.get(url)
    if (r.status_code != 200):
    # if the user press enter then the endgame will be an empty str & go inside the loop for a new question
    # if the user types quit its going to jump out of the loop
        endGame = input("Sorry there was aproblem retrieving the question. Press enter to try again or type 'quit' to quit the game.")
    else:

        # variable to validate the end user answers
        valid_answer = False
        # all answers will be numbered & will increment depending on the No of answers
        answer_number = 1
        data = json.loads(r.text)
        question = data['results'][0]['question']
        answers = data['results'][0]['incorrect_answers']
        correct_answer = data['results'][0]['correct_answer']
        # append the correct answers to incorrects ones because one is a list and the other one is string
        answers.append(correct_answer)
        # to shuffle the array so the correct answer is the last one
        random.shuffle(answers)

        print(html.unescape(question) + "\n")

        for answer in answers:
            print(str(answer_number) + "-" + html.unescape(answer))
            answer_number += 1

        while valid_answer == False:
            # store the users answers in a variable
            user_answer = input("\nType the number of the correct answer: ")
            try:
                user_answer = int(user_answer)
                if user_answer > len(answers) or user_answer <= 0:
                    print("Invalid answer")
                else:
                    valid_answer = True
            except:
                print("Invalid answer. Use only numbers.")
            
        # the first element of the list is not index 1 but hence the -1
        user_answer = answers[int(user_answer)-1]

        if user_answer == correct_answer:
            print("\nCongrats ! you answered correctly ! the correct answer was: " + html.unescape(correct_answer) )
            score_correct += 1
        else:
            print("Sorry, " + html.unescape(user_answer) + " is incorrect. The correct answer is: " + html.unescape(correct_answer))
            score_correct += 1
            
        print("\n##########################")
        print("Your score is:")
        print("Correct answers: " + str(score_correct))
        print("Incorrect answers: " + str(score_incorrect))
        print("##########################")
                    
        endGame = input("\nPress enter to play again or type 'quit' to quit the game.").lower()

print("\nThanks for playing")        
        

