# Star Pattern Generator
# Topics: loops, nested loops, conditional statements, output

rows = int(input("Enter number of rows: "))

if rows <= 0:
    print("Please enter a positive number")
else:
    for i in range(1, rows + 1):
        for j in range(i):
            print("*", end="")
        print()
