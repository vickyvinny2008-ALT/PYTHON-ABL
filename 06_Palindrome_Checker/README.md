# Palindrome Checker

**Syllabus mapping:** Unit II: strings, string methods, slicing and if-else.

## 1. Problem statement
Check whether a word or phrase is a palindrome, ignoring spaces and uppercase/lowercase differences.

## 2. Objectives
- Normalize a string using string methods.
- Reverse a string using slicing.
- Compare strings using if-else.

## 3. Assumptions
- Only spaces and letter case are ignored.
- Punctuation is not removed.

## 4. Algorithm
1. Start.
2. Input a word or phrase.
3. Convert the text to lowercase and remove spaces.
4. Reverse the cleaned string.
5. Compare the cleaned string with its reverse.
6. Display the result.
7. Stop.

## 5. Flowchart representation
```text
START → Input text → Lowercase and remove spaces → Reverse → Compare → Display result → STOP
```

## 6. Pseudocode
```text
START
INPUT text
cleaned = text.lower().replace(' ', '')
reversed_text = reverse of cleaned
IF cleaned = reversed_text: display palindrome
ELSE display not palindrome
STOP
```

## 7. Python source code
See [main.py](./main.py).

```python
# Palindrome Checker
text = input("Enter a word or phrase: ")
cleaned = text.lower().replace(" ", "")
reversed_text = cleaned[::-1]

if cleaned == reversed_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
```

## 8. Test cases

| Input / Test | Expected result |
|---|---|
| Madam | It is a palindrome |
| nurses run | It is a palindrome |
| Python | It is not a palindrome |

## 9. Sample console output
```text
Enter a word or phrase: nurses run
It is a palindrome
```

## 10. Conclusion
This program uses string methods, slicing and conditional comparison to identify palindromes.

## How to run
Open a terminal in this folder and run:

```bash
python main.py
```
