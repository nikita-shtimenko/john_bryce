def main():
    max_number = 0

    while True:
        number = int(input("Enter next number: "))

        if number <= 0:
            break

        if number > max_number:
            max_number = number

    print(f"Max number = {max_number}")
    return 1


if __name__ == '__main__':
    main()