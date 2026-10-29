# String Analyzer

**Syllabus mapping:** Unit II: strings, string methods, for loop and membership testing.

## 1. Problem statement
Read a line of text and display its length, uppercase form, lowercase form, number of vowels and number of digits.

## 2. Objectives
- Use string methods.
- Traverse a string character by character.
- Count vowels and digits with conditions.

## 3. Assumptions
- Spaces and punctuation are allowed.
- Vowels are a, e, i, o and u, ignoring case.

## 4. Algorithm
1. Start.
2. Input a line of text.
3. Initialize vowel and digit counters to zero.
4. Visit each character.
5. Increment vowel count if the character is a vowel.
6. Increment digit count if the character is a digit.
7. Display the length, case conversions and counts.
8. Stop.

## 5. Flowchart representation
```text
START → Input text → Initialize counters → Loop through characters → Count vowels/digits → Display analysis → STOP
```

## 6. Pseudocode
```text
START
INPUT text
vowels = 0; digits = 0
FOR each character ch in text
IF ch.lower() belongs to 'aeiou': vowels = vowels + 1
IF ch.isdigit(): digits = digits + 1
DISPLAY length, uppercase, lowercase, vowels, digits
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# String Analyzer
text = input("Enter a line of text: ")
vowel_count = 0
digit_count = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowel_count += 1
    if ch.isdigit():
        digit_count += 1

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Vowels:", vowel_count)
print("Digits:", digit_count)
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| Hello123 | Length 8; vowels 2; digits 3 |
| PYTHON | Vowels 1; digits 0 |
| AEIOU | Vowels 5; digits 0 |

## 9. Sample console output
```text
Enter a line of text: Hello123
Length: 8
Uppercase: HELLO123
Lowercase: hello123
Vowels: 2
Digits: 3
```

## 10. Conclusion
This program demonstrates string traversal, string methods, membership testing and conditional counting.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
