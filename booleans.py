# booleans & conditionals
# create a program and store your age in a variable
# ask the user for his age and print whether:
#  - he's older than you
#  - he's younger than you
# - you two have the same age

my_age = 30
user_age = int(input("Type your age: "))
    
if (user_age > my_age):
    print("You're older than me")
elif (user_age == my_age):
    print("we are the same age")
else:
    print("you're younger than me")
    
