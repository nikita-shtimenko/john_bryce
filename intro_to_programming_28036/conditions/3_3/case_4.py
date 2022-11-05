def main():
    year = int(input("Enter a year"))
    return ["True" if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else "False"]


if __name__ == '__main__':
    main()