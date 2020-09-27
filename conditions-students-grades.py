# nested if structure
# rules:
# - grades are 0 to 10
# - students need an avg grade of 6 or higher to get approval
# - students need an attendance rate of 80% or higher to get approval

grade1 = float (input("Type the grade of the first test: "))
grade2 = float (input("Type the grade of the second test: "))
absences = int (input("Type the number of absences: "))
total_classes = int (input("Type the total number of classes: "))


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
    print("the student has failed duw to an avg grade lower than 6.0.")
else:
    print("the student has failed duw to an avg grade lower than 6.0 & attendance lower than 80%.")
    
