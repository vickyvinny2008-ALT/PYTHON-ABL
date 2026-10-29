# List Statistics Calculator

**Syllabus mapping:** Unit III: list creation, append, traversal and list operations.

## 1. Problem statement
Read a set of numbers into a list and calculate their sum, average, largest value and smallest value.

## 2. Objectives
- Create and update a list using append().
- Traverse input values using a loop.
- Calculate basic statistics.

## 3. Assumptions
- At least one number must be entered.
- All values are numeric.

## 4. Algorithm
1. Start.
2. Input the count n.
3. If n is not positive, display an error.
4. Create an empty list and read n values into it.
5. Calculate sum, average, maximum and minimum.
6. Display the list and statistics.
7. Stop.

## 5. Flowchart representation
```text
START → Input count → Validate → Read values into list → Calculate statistics → Display results → STOP
```

## 6. Pseudocode
```text
START
INPUT n
IF n <= 0: display error
ELSE create empty list numbers
REPEAT n times: INPUT value; APPEND value
total = sum(numbers); average = total / n
DISPLAY numbers, total, average, max(numbers), min(numbers)
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# List Statistics Calculator
n = int(input("How many numbers? "))

if n <= 0:
    print("Enter a positive count")
else:
    numbers = []
    for i in range(n):
        value = float(input("Enter number: "))
        numbers.append(value)

    total = sum(numbers)
    average = total / len(numbers)

    print("List:", numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Largest:", max(numbers))
    print("Smallest:", min(numbers))
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| 2, 4, 6, 8 | Sum 20; Average 5; Largest 8; Smallest 2 |
| 7 | Sum 7; Average 7; Largest 7; Smallest 7 |

## 9. Sample console output
```text
How many numbers? 4
Enter number: 2
Enter number: 4
Enter number: 6
Enter number: 8
List: [2.0, 4.0, 6.0, 8.0]
Sum: 20.0
Average: 5.0
Largest: 8.0
Smallest: 2.0
```

## 10. Conclusion
This program demonstrates list creation, appending elements and calculating statistics using list operations.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
