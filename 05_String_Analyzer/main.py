# String Analyzer
# Topics: strings, loops, string methods, conditions, input/output

text = input("Enter a line of text: ")
vowel_count = 0
digit_count = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowel_count = vowel_count + 1
    if ch.isdigit():
        digit_count = digit_count + 1

print("Length:", len(text))
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Vowels:", vowel_count)
print("Digits:", digit_count)
