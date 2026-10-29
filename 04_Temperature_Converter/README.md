# Temperature Converter

**Syllabus mapping:** Unit I: input/output, type conversion and expressions; Unit II: conditions.

## 1. Problem statement
Create a program that converts Celsius to Fahrenheit or Fahrenheit to Celsius based on the user's choice.

## 2. Objectives
- Accept a conversion choice and temperature.
- Apply the correct conversion formula.
- Display the converted temperature.

## 3. Assumptions
- The temperature is numeric.
- Choice must be 1 or 2.

## 4. Algorithm
1. Start.
2. Display conversion options.
3. Input the choice and temperature.
4. For choice 1, calculate F = C × 9/5 + 32.
5. For choice 2, calculate C = (F − 32) × 5/9.
6. Display the result or invalid-choice message.
7. Stop.

## 5. Flowchart representation
```text
START → Display menu → Input choice and temperature → Apply selected formula → Display result → STOP
```

## 6. Pseudocode
```text
START
DISPLAY conversion menu
INPUT choice, temperature
IF choice = 1: converted = temperature * 9 / 5 + 32
ELSE IF choice = 2: converted = (temperature - 32) * 5 / 9
ELSE display invalid choice
DISPLAY converted value if choice is valid
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# Temperature Converter
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
choice = input("Enter choice (1 or 2): ")
temperature = float(input("Enter temperature: "))

if choice == "1":
    converted = temperature * 9 / 5 + 32
    print("Temperature in Fahrenheit:", converted)
elif choice == "2":
    converted = (temperature - 32) * 5 / 9
    print("Temperature in Celsius:", converted)
else:
    print("Invalid choice")
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| Celsius 0 | 32.0 Fahrenheit |
| Fahrenheit 212 | 100.0 Celsius |
| Choice 3 | Invalid choice |

## 9. Sample console output
```text
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
Enter choice (1 or 2): 1
Enter temperature: 0
Temperature in Fahrenheit: 32.0
```

## 10. Conclusion
This program uses mathematical expressions, type conversion and conditional statements.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
