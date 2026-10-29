# Student Marks and Grade Calculator

**Syllabus mapping:** Unit I: variables, arithmetic and type conversion; Unit II: if-elif-else; Unit III: lists.

## 1. Problem statement
Accept marks for five subjects, calculate total and percentage, and assign a grade using the stated grading scale.

## 2. Objectives
- Store subject marks in a list.
- Calculate total and percentage.
- Use conditional statements to assign a grade.

## 3. Assumptions
- Each subject is out of 100 marks and has equal weight.
- Grade scale: 90+ A, 80–89 B, 70–79 C, 60–69 D, below 60 F.

## 4. Algorithm
1. Start.
2. Read five marks into a list.
3. Validate that all marks are between 0 and 100.
4. Calculate total and percentage.
5. Use an if-elif-else ladder to determine the grade.
6. Display total, percentage and grade.
7. Stop.

## 5. Flowchart representation
```text
START → Input five marks → Validate range → Calculate total and percentage → Determine grade → Display result → STOP
```

## 6. Pseudocode
```text
START
CREATE empty list marks
REPEAT five times: INPUT mark; APPEND mark
IF any mark < 0 OR any mark > 100: display invalid marks
ELSE calculate total and percentage
Use if-elif-else to assign grade
Display total, percentage and grade
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
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
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| 90, 80, 70, 85, 75 | Total 400; Percentage 80%; Grade B |
| 100, 95, 92, 90, 98 | Total 475; Percentage 95%; Grade A |
| 110, 80, 70, 60, 50 | Invalid marks message |

## 9. Sample console output
```text
Enter marks for subject 1: 90
Enter marks for subject 2: 80
Enter marks for subject 3: 70
Enter marks for subject 4: 85
Enter marks for subject 5: 75
Total: 400.0 out of 500
Percentage: 80.0 %
Grade: B
```

## 10. Conclusion
This program applies list operations, arithmetic and conditional statements to calculate a student's result.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
