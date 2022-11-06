def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    numbers = [i for i in range(first_number, second_number + 1)]
    numbers += [i for i in range(second_number - 1, first_number - 1, -1)]

    return print(numbers)

if __name__ == '__main__':
    main()