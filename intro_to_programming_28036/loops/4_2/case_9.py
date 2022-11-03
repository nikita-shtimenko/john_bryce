def main():
    index = 1
    max_number = 0
    max_number_index = 0

    while index <= 10:
        number = int(input("Enter number: "))

        if number > max_number:
            max_number = number
            max_number_index = index

        index += 1

    print(f"Max number = {max_number}, index = {max_number_index}")
    return 1


if __name__ == '__main__':
    main()