def main():
    year = int(input("Enter a year"))

    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("True")
    
    print("False")
    return 1


if __name__ == '__main__':
    main()