# Student Record Using Tuples

**Syllabus mapping:** Unit III: tuples, tuple access and unpacking; Unit II: conditions.

## 1. Problem statement
Store a student's roll number, name and marks in a tuple, unpack the tuple and display the record with a pass/fail result.

## 2. Objectives
- Create a tuple of related values.
- Use tuple unpacking.
- Apply a simple condition to marks.

## 3. Assumptions
- The record contains roll number, name and marks.
- A mark of 40 or above is considered a pass for this example.

## 4. Algorithm
1. Start.
2. Input roll number, name and marks.
3. Create a tuple from the values.
4. Unpack the tuple into variables.
5. Display the record.
6. Display Pass if marks are at least 40; otherwise display Fail.
7. Stop.

## 5. Flowchart representation
```text
START → Input student details → Create tuple → Unpack tuple → Display record → Check marks → Display Pass/Fail → STOP
```

## 6. Pseudocode
```text
START
INPUT roll_no, name, marks
student = (roll_no, name, marks)
UNPACK student into roll_no, name, marks
DISPLAY student details
IF marks >= 40: DISPLAY Pass
ELSE DISPLAY Fail
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
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
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| 101, Ravi, 75 | Result: Pass |
| 102, Sita, 32 | Result: Fail |

## 9. Sample console output
```text
Enter roll number: 101
Enter student name: Ravi
Enter marks: 75
Student Record
Roll Number: 101
Name: Ravi
Marks: 75.0
Result: Pass
```

## 10. Conclusion
This program demonstrates tuple creation, tuple unpacking, displaying data and conditional statements.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
