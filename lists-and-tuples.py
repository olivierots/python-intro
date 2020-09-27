# Exercise: Lists 7 tuples
# Create a program that asks the user for his birthday in the below format
# "DD-MM-YYYY. then print:
# you were born in [month]"
# e.g " You were born in january"

# tuple to get the corresponding month
months = ("january", "february", "march", "may", "june", "july", "august", "september", "october", "november", "december")

birthday = input("Type your birthday in the format DD-MM_YYYY: ")

# variable as an index of the tuple
# index = birthday [3:5] ==> this will a str so its got to be converted to an int
# in order to use it as an index
# indexes start from 0 hence why we use -1 

index = int(birthday[3:5]) -1
bd_month = months[index]

print("you were born in ", bd_month)
