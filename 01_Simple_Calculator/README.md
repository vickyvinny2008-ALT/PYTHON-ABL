# Simple Arithmetic Calculator

**Syllabus mapping:** Unit I: input/output, type conversion and arithmetic operators; Unit II: if-elif-else.

## 1. Problem statement
Write a program that accepts two numbers and an arithmetic operator, then displays the calculation result. It must handle division by zero and unsupported operators.

## 2. Objectives
- Accept user input and convert numeric values using float().
- Apply arithmetic operators and an if-elif-else ladder.
- Handle division by zero and invalid operators.

## 3. Assumptions
- The two operands are valid numbers.
- Only +, -, * and / are supported.

## 4. Algorithm
1. Start.
2. Read the first number, operator and second number.
3. Check the operator and perform the corresponding calculation.
4. If division is selected with a zero divisor, display an error.
5. If the operator is unsupported, display an invalid-operator message.
6. Otherwise display the result and stop.

## 5. Flowchart representation
```text
START → Input a, operator, b → Check operator → Calculate or handle error → Display result/message → STOP
```

## 6. Pseudocode
```text
START
INPUT a, operator, b
IF operator = '+' THEN result = a + b
ELSE IF operator = '-' THEN result = a - b
ELSE IF operator = '*' THEN result = a * b
ELSE IF operator = '/' AND b != 0 THEN result = a / b
ELSE display appropriate error
IF result is valid THEN display result
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# Simple Arithmetic Calculator
a = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
b = float(input("Enter second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b != 0:
        result = a / b
    else:
        result = None
        print("Error: division by zero")
else:
    result = None
    print("Invalid operator")

if result is not None:
    print("Result:", result)
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| 8 + 2 | Result: 10.0 |
| 9 / 0 | Error: division by zero |
| 5 * 3 | Result: 15.0 |

## 9. Sample console output
```text
Enter first number: 8
Enter operator (+, -, *, /): +
Enter second number: 2
Result: 10.0
```

## 10. Conclusion
This program demonstrates input/output, type conversion, arithmetic operators and conditional decision making.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
