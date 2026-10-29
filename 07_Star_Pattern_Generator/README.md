# Star Pattern Generator

**Syllabus mapping:** Unit II: for loop, nested loops and pattern generation.

## 1. Problem statement
Print a right-angled triangle pattern of stars for the number of rows entered by the user.

## 2. Objectives
- Use nested loops to generate a pattern.
- Understand outer-loop and inner-loop repetition.
- Control the number of rows.

## 3. Assumptions
- The number of rows must be a positive integer.
- Each row contains one more star than the previous row.

## 4. Algorithm
1. Start.
2. Input the number of rows.
3. If rows are not positive, display an error.
4. For each row from 1 to rows, print that number of stars.
5. Move to a new line after each row.
6. Stop.

## 5. Flowchart representation
```text
START → Input rows → Validate positive value → Outer loop → Inner loop prints stars → New line → STOP
```

## 6. Pseudocode
```text
START
INPUT rows
IF rows <= 0: display error
ELSE FOR i from 1 to rows
  FOR j from 1 to i: PRINT '*' without newline
  PRINT newline
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# Star Pattern Generator
rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Please enter a positive number")
else:
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| 3 rows | *, **, *** on separate lines |
| 1 row | * |
| 0 rows | Please enter a positive number |

## 9. Sample console output
```text
Enter number of rows: 4
*
**
***
****
```

## 10. Conclusion
This program demonstrates nested for loops, range() and output formatting.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
