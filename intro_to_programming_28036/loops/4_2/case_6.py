def main():
    numbers_sum = 0
    numbers_count = 0

    while True:
        number = int(input("Enter next number: "))

        if number == 0:
            break

        numbers_sum += number
        numbers_count += 1

    print(f"Numbers average = {numbers_sum / numbers_count}, numbers count = {numbers_count}")
    return 1


if __name__ == '__main__':
    main()