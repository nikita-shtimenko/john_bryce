def main():
    year = int(input("Enter a year"))
    month = int(input("Enter month number (1 - 12): "))

    if month not in range(1, 12 + 1):
        print("Error: month has to be in range from 1 to 12.")
        return main()

    month_days = (
        31,
        (28, 29),
        31,
        30,
        31,
        30,
        31,
        31,
        30,
        31,
        30,
        31
    )

    result = 0

    if month == 2:
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            result = month_days[month - 1][1]
        else:
            result = month_days[month - 1][0]
    else:
        result = month_days[month - 1]

    print(result)
    return 1


if __name__ == '__main__':
    main()