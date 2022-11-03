def main():
    numbers_sum = 0

    while True:
        number = int(input("Enter next number (-99 to stop): "))

        if number < 0:
            if number == -99:
                break

            print("You can enter only positive numbers")
            continue

        numbers_sum += number

    print(f"Numbers sum = {numbers_sum}")
    return 1


if __name__ == '__main__':
    main()