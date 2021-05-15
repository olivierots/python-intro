# exercise: error handling
# apply the try and except statemens to the students grades program
# and keep it from crashing

# rules:
# - grades are 0 to 10
# - students need an avg grade of 6 or higher to get approval
# - students need an attendance rate of 80% or higher to get approval
# implementent data validation too


###### grade 1 section ######
data_valid = False
while data_valid == False:
    grade1 = input("Type the grade of the first test: ")

    ## validate if its a valid number
    try:
        grade1 = float(grade1)
    except:
        print("invalid input. only numbers ar accepted. decimals should be separated with a dot.")
        continue

    ## validate if this number is within the range we want between 0 & 10 
    if grade1 < 0 or grade1 > 10:
        print("grade should be be between 0 and 10")
        continue
    else:
        data_valid = True


###### grade 2 section ######
data_valid = False
while data_valid == False:
    grade2 = input("Type the grade of the 2nd test: ")
    ## validate if its a valid number
    try:
        grade2 = float(grade2)
    except:
        print("invalid input. only numbers are accepted. decimals should be separated with a dot.")
        continue
    
    ## validate if this number is within the range we want 
    if grade2 < 0 or grade1 > 10:
        print("grade should be be between 0 and 10")
        continue
    else:
        data_valid = True

###### total number of classes section ######
data_valid = False
while data_valid == False:
    total_classes = input("Type the total number of classes: ")

    ## validate whether this is a valid number
    try:
        total_classes = int(total_classes)
    except:
        print("invalid input. only numbers are accepted.")
        continue

    ## validate if this number is within the range we want 
    if total_classes < 0:
        print("the No of classes cant be 0 or less")
        continue
    else:
        data_valid = True        

###### number of absences section ######
data_valid = False
while data_valid == False:
    absences = input("Type the number of absences: ")

    ## validate whether this is a valid number
    try:
        absences = int(absences)
    except:
        print("invalid input. only numbers are accepted.")
        continue
    
    ## validate if this number is within the range we want
    if absences < 0 or absences > total_classes:
        print("the No of absences cant be less than 0 or greater than the No of total classes")
        continue
    else:
        data_valid = True     


avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes


print ("Average grade: ", round(avg_grade,2))
print ("Attendance rate: ", str(round((attendance * 100),2))+'%' )
# we use string to so we can concatenate with % sign


if (avg_grade >= 6):
    if (attendance >= 0.8):
        print("the student has been approved.")
    else:
        print("the student has failed due to attendance rate lower than 80%.")
elif (attendance >= 0.8):
    print("the student has failed due to an avg grade lower than 6.0.")
else:
    print("the student has failed duw to an avg grade lower than 6.0 & attendance lower than 80%.")
    
