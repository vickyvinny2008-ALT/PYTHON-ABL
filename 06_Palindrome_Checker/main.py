# Palindrome Checker
text = input("Enter a word or phrase: ")
cleaned = text.lower().replace(" ", "")
reversed_text = cleaned[::-1]

if cleaned == reversed_text:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
