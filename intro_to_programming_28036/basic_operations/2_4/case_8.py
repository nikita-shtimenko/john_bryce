def main():
    number = int(input("Enter 2-digit number (from 10 to 99): "))

    if number not in range(10, 99 + 1):
        print("Error: number has to be in range from 10 to 99.")
        return main()

    print(f"Number = {number}, digits sum = {(number // 10) + (number % 10)}")
    return 1


if __name__ == '__main__':
    main()