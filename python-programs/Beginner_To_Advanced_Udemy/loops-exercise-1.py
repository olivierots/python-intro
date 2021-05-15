# create a program that asks a user for 8 names of people and store them in a list.
# when all the names have been given, pick a random one and print it out

import random

people = []
for x in range(0,8):
    person = input ("type the name of a person: ")
    people.append(person)
    
index = random.randint(0,7)
random_person = people[index]

print("picking a random person: ", random_person) 

    
