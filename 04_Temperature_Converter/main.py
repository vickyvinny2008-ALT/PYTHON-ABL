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
