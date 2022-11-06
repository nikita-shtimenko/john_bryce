def main():
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("Error: you have to enter a number.")
        return main()

    digits = list(map(int, str(number)))
    digits.sort()

    print(digits) 
    return 1


if __name__ == '__main__':
    main()