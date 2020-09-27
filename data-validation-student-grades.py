# rules:
# - grades are 0 to 10
# - students need an avg grade of 6 or higher to get approval
# - students need an attendance rate of 80% or higher to get approval
# implementent data validation too


data_valid = False
while data_valid == False:
    grade1 = float (input("Type the grade of the first test: "))
    if grade1 < 0 or grade1 > 10:
        print("grade should be be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    grade2 = float (input("Type the grade of the 2nd test: "))
    if grade2 < 0 or grade1 > 10:
        print("grade should be be between 0 and 10")
        continue
    else:
        data_valid = True

data_valid = False
while data_valid == False:
    total_classes = int (input("Type the total number of classes: "))
    if total_classes < 0:
        print("the No of classes cant be 0 or less")
        continue
    else:
        data_valid = True        

data_valid = False
while data_valid == False:
    absences = int (input("Type the number of absences: "))
    if absences < 0 or absences > total_classes:
        print("the No of absences cant be less than 0 or greater than the No of total classes")
        continue
    else:
        data_valid = True     

absences = int (input("Type the number of absences: "))

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
    
