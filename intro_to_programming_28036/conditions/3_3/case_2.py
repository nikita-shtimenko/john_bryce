def main():
    grade = int(input("Enter your grade: "))

    if grade < 55:
        print("בלתי מספיק")
    elif grade >= 55 and grade <= 64:
        print("מספיק")
    elif grade >= 65 and grade <= 74:
        print("כמעט טוב")
    elif grade >= 75 and grade <= 84:
        print("טוב")
    elif grade >= 85 and grade <= 94:
        print("טוב מאד")
    elif grade >= 95:
        print("מצוין")
        
    return 1


if __name__ == '__main__':
    main()