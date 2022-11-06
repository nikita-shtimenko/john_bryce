def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    return print([i for i in range(first_number, second_number + 1)])

if __name__ == '__main__':
    main()