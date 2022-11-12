"""
    Option 1
"""
text = input("Enter text: ")

if text.endswith("a") or text.endswith("e") or text.endswith("i") \
    or text.endswith("o") or text.endswith("u") or text.endswith("y"):
    print("Vowel")
else:
    print("Not vowel")

"""
    Option 2
"""
text = input("Enter text: ")
print("Vowel" if text[len(text) - 1] in ['a', 'e', 'i', 'o', 'u', 'y'] else "Not vowel")