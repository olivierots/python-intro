# create a program to calculate the BMI (body mass index) of a person.
# ask the user for his height in meters and his weight in kg

# BMI formula = weight / (height * height )
# weight in kg and height in meters

# in case you want to use inches and feet for height and pounds for the weight use the below
# BMI = (weight / (height * height))*703
# weight in pounds
# height in inches
# 1 foot = 12 inches

# print the BMI and classification
# less than or equal to 18.5: UNDERWEIGHT
# greater than 18.5 or less than or equal to 24.9: NORMAL WEIGHT
# greater than 24.9 or less than or equals to 29.9: OVERWEIGHT
# greater than or equal to 30: OBESITY

print("this program calculates your body mass index.")

weight = float ( input("Type your weight in kg (ex. 70.5): ") )
height = float ( input("Type your height in meters (ex. 1.70): ") )
bmi = weight / (height ** 2)
print ("Your BMI is: ",round(bmi,2))

if (bmi <= 18.5):
    classification = "UNDERWEIGHT"
elif (bmi > 18.5 and bmi <= 24.9):
    classification = "NORMAL WEIGHT"
elif (bmi > 24.9 and bmi <= 29.9):
    classification = "OVERWEIGHT"
else:
    classification = "OBESITY"

print ("the classificartion of your bmi is:" , classification) 
