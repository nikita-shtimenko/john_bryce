grade = int(input("Enter your grade: "))

if grade < 55:
    print("Not enough")
elif 55 <= grade <= 64:
    print("Enough")
elif 65 <= grade <= 74:
    print("Almost good")
elif 75 <= grade <= 84:
    print("Good")
elif 85 <= grade <= 94:
    print("Very good")
elif grade >= 95:
    print("Excellent")