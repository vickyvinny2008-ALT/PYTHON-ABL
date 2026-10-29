# Student Marks and Grade Calculator
marks = []
for i in range(1, 6):
    mark = float(input("Enter marks for subject " + str(i) + ": "))
    marks.append(mark)

if min(marks) < 0 or max(marks) > 100:
    print("Invalid marks. Enter marks from 0 to 100.")
else:
    total = sum(marks)
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
