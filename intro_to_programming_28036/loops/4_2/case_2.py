def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    while first_number <= second_number:
        print(first_number)
        first_number += 1

    return 1


if __name__ == '__main__':
    main()