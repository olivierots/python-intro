# create a guess game with the names of the colors, at each round pick a random color from
# a list and let the user try to guess it. when he does it, ask if he wants to play again.
# keep playing until the user types "no".

import random

colors = ["white", "black", "red", "green", "blue", "yello", "purple", "grey"]
while True:
    color = colors[random.randint(0,len(colors)-1)]
    guess = input("I'm thinking about a color, can you guess it: ")

    while True:
        if (color ==guess.lower()):
            break
        else:
            # this will still run untill the person guess right
            guess = input("Nope. Try again: ")
    print("you guessed it ! i was thinking about", color)

    play_again = input("Let's play again ? Type 'no' to quit.")
    if play_again.lower() == 'no':
          break
print("it was fun ! thanks for playing")        

    
