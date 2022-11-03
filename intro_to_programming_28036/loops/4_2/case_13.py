def main():
    number = int(input("Enter number: "))
    dig = int(input("Enter dig: "))

    number_digits = list(map(int, str(number)))
    
    print(f"Digit {dig} appears {number_digits.count(dig)} time(s) in number {number}.")
    return 1


if __name__ == '__main__':
    main()