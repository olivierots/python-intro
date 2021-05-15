import random
number = random.randint(0,10)
guess = int (input("I'm thinking about a numberbetween 0 & 10. Can you guess it? " ) )

while True:
    if guess == number:
       break
    else:
        guess = int (input ("Nope. Try again: "))
print("You guessed right. I was thinking about", number)
