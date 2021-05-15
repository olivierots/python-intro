# create a program with a predefined dictionary for a person. include the follwing info:
# name, gender, age, address and phone
# ask the user what info he want to know about the person (example:"name"), then
# print the value associated to that key or display a message in case the key isnt found
# .lower() bypass the case issue e.g a user types in Name or NAME or name etc


person = { "name": "Jon Green", "gender": "M", "age": "35", "address": " 2 smiles Place", "phone": "07384848" }
key = input("what information would you like to know about this person? ").lower()
result = person.get(key, "that info is not available")
           
print(result)
