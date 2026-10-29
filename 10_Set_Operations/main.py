# Set Operations and Duplicate Removal
a = set(map(int, input("Enter first group of integers: ").split()))
b = set(map(int, input("Enter second group of integers: ").split()))

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
