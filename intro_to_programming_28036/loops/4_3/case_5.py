def main():
    number = int
    non_primary_count = 0
    is_primary = True
    temp_number = 1

    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Error: you have to enter a number.")
            continue

        temp_number = 1
        is_primary = True

        while temp_number <= number:
            if temp_number != 1 and temp_number != number:
                if number % temp_number == 0:
                    is_primary = False
                    non_primary_count += 1
                    break

            temp_number += 1

        if is_primary and number != 1:
            print(f"Entered primary number: {number}")
            break

    print(f"Non-primary numbers count: {non_primary_count}")
    return 1


if __name__ == '__main__':
    main()