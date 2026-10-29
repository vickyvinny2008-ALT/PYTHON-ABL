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
