# Palindrome Checker
# Topics: strings, loops, string methods, conditionals

text = input("Enter a word or phrase: ")
cleaned = text.lower().replace(" ", "")
reversed_text = ""

# Build the reversed string using a loop instead of slicing.
for ch in cleaned:
    reversed_text = ch + reversed_text

if cleaned == reversed_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
