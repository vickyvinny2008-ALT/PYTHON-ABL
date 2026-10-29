# List Statistics Calculator
# Topics: lists, loops, arithmetic, input/output, conditions

n = int(input("How many numbers? "))

if n <= 0:
    print("Enter a positive count")
else:
    numbers = []
    for i in range(n):
        value = float(input("Enter number: "))
        numbers.append(value)

    total = 0
    largest = numbers[0]
    smallest = numbers[0]

    for value in numbers:
        total = total + value
        if value > largest:
            largest = value
        if value < smallest:
            smallest = value

    average = total / len(numbers)

    print("List:", numbers)
    print("Sum:", total)
    print("Average:", average)
    print("Largest:", largest)
    print("Smallest:", smallest)
