def main():
    min_number = -1

    while True:
        number = int(input("Enter next number: "))

        if number <= 0:
            break

        if number < min_number:
            min_number = number

    print(f"Min number = {min_number}")
    return 1


if __name__ == '__main__':
    main()