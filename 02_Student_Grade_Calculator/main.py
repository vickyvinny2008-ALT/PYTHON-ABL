# Student Marks and Grade Calculator
# Topics: lists, loops, input/output, type conversion, arithmetic, conditions

marks = []
valid = True

for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    if mark < 0 or mark > 100:
        valid = False
    marks.append(mark)

if not valid:
    print("Invalid marks. Enter marks from 0 to 100.")
else:
    total = 0
    for mark in marks:
        total = total + mark

    percentage = total / 5

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    print("Total:", total, "out of 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)
