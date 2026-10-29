# Set Operations and Duplicate Removal

**Syllabus mapping:** Unit III — sets, union, intersection, difference and membership testing.

## 1. Problem statement
Read two groups of integers, remove duplicates by converting them to sets, and display their union, intersection, difference and a membership result.

## 2. Objectives
- Create sets from user input.
- Perform union, intersection and difference.
- Use the `in` operator for membership testing.

## 3. Assumptions
- Integers are entered separated by spaces.
- Duplicate values appear only once in each set.
- The order of displayed set elements may vary.

## 4. Algorithm
1. Start.
2. Read two lines of integers.
3. Convert each line to a set.
4. Display both sets, union, intersection and A minus B.
5. Read a number to search in Set A.
6. Use membership testing and display the result.
7. Stop.

## 5. Flowchart representation
```text
START → Input two groups → Convert to sets
→ Calculate union/intersection/difference
→ Input search number → Test membership
→ Display results → STOP
```

## 6. Pseudocode
```text
START
INPUT line1, line2
A = set of integers from line1
B = set of integers from line2
DISPLAY A union B
DISPLAY A intersection B
DISPLAY A difference B
INPUT x
IF x in A: display present
ELSE display not present
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
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
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| A: 1 2 2 3; B: 2 3 4; search 1 | Union {1,2,3,4}; intersection {2,3}; A-B {1}; present |
| A: 5 6; B: 6 7; search 9 | Union {5,6,7}; intersection {6}; A-B {5}; not present |

## 9. Sample console output
```text
Enter first group of integers: 1 2 2 3
Enter second group of integers: 2 3 4
Set A: {1, 2, 3}
Set B: {2, 3, 4}
Union: {1, 2, 3, 4}
Intersection: {2, 3}
A - B: {1}
Enter a number to search in Set A: 1
1 is present in Set A
```

## 10. Conclusion
This program demonstrates set creation, automatic duplicate removal, set operations and membership testing.

## Run
```bash
python main.py
```
