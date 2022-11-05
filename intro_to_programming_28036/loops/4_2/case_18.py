def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    result = divmod(first_number, second_number)

    print(result[0], result[1])
    return 1


if __name__ == '__main__':
    main()