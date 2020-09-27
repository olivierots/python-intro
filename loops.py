x = 0
people = []

#while x < 5:
while len(people) < 5:
    person = input("type a name of a person: ")
    people.append(person)
    x = x + 1 # or x += 1 increment operator
print(people)
