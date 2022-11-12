"""
    Option 1
"""
text = input("Enter text: ")

if text.isspace():
    print("Spaces")
else:
    print("Not spaces")

"""
    Option 1
"""
text = input("Enter text: ")
print("Spaces" if text.isspace() else "Not spaces")