"""
    Option 1
"""
text = input("Enter text: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not palindrome")

"""
    Option 2
"""
text = input("Enter text: ")
print("Palindrome" if text == text[::-1] else "Not palindrome")