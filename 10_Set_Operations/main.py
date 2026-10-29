# Set Operations and Duplicate Removal
# Topics: sets, input/output, type conversion, loops, membership and set operations

first_values = input("Enter first group of integers: ").split()
second_values = input("Enter second group of integers: ").split()

a = set()
b = set()

for value in first_values:
    a.add(int(value))

for value in second_values:
    b.add(int(value))

print("Set A:", a)
print("Set B:", b)
print("Union:", a | b)
print("Intersection:", a & b)
print("A - B:", a - b)

x = int(input("Enter a number to search in Set A: "))
if x in a:
    print(x, "is present in Set A")
else:
    print(x, "is not present in Set A")
