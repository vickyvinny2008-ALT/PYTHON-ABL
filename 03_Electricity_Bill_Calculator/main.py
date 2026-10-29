# Electricity Bill Calculator
# Illustrative rates for this assignment; not an official tariff.
# Topics: input/output, type conversion, arithmetic, conditional statements

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
