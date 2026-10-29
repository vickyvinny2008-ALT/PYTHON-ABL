# Student Record Using Tuples
roll_no = input("Enter roll number: ")
name = input("Enter student name: ")
marks = float(input("Enter marks: "))

student = (roll_no, name, marks)
roll_no, name, marks = student

print("Student Record")
print("Roll Number:", roll_no)
print("Name:", name)
print("Marks:", marks)

if marks >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
