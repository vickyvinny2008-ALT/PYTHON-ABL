# Electricity Bill Calculator

**Syllabus mapping:** Unit I: arithmetic and input/output; Unit II: conditional statements.

## 1. Problem statement
Calculate an electricity bill using illustrative slab rates: first 100 units at ₹1.50 each, next 100 at ₹2.50 each, and units above 200 at ₹4.00 each.

## 2. Objectives
- Accept units consumed.
- Calculate charges using slab-wise conditions.
- Display the bill amount.

## 3. Assumptions
- Rates are illustrative for learning, not an official tariff.
- Negative units are invalid.
- No taxes or fixed charges are included.

## 4. Algorithm
1. Start.
2. Input units consumed.
3. If units are negative, display invalid input.
4. For up to 100 units, multiply by 1.50.
5. For 101–200 units, charge ₹150 plus ₹2.50 for each unit above 100.
6. Above 200 units, charge ₹400 plus ₹4.00 for each unit above 200.
7. Display the bill and stop.

## 5. Flowchart representation
```text
START → Input units → Validate units → Apply appropriate slab → Display bill → STOP
```

## 6. Pseudocode
```text
START
INPUT units
IF units < 0: display invalid units
ELSE IF units <= 100: bill = units * 1.50
ELSE IF units <= 200: bill = 150 + (units - 100) * 2.50
ELSE: bill = 400 + (units - 200) * 4.00
DISPLAY bill
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# Electricity Bill Calculator
# Illustrative rates for this assignment; not an official tariff.
units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units")
elif units <= 100:
    bill = units * 1.50
    print("Electricity bill: Rs.", bill)
elif units <= 200:
    bill = 150 + (units - 100) * 2.50
    print("Electricity bill: Rs.", bill)
else:
    bill = 400 + (units - 200) * 4.00
    print("Electricity bill: Rs.", bill)
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| 80 units | Rs. 120.0 |
| 150 units | Rs. 275.0 |
| 250 units | Rs. 600.0 |

## 9. Sample console output
```text
Enter electricity units consumed: 150
Electricity bill: Rs. 275.0
```

## 10. Conclusion
This program demonstrates arithmetic calculations and multi-branch decision making.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
