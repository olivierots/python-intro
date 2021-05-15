# create a program with a predefined list of people
# ask the user for his name, add it to the end of the list
# and print the updated list

people = ["john","mary","peter"]
user = input("type your name: ")
people.append(user)
print("here's the list: ", people)
