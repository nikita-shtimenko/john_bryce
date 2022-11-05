def main():
    number = int(input("Enter number (from 1000 to 9999): "))

    if number not in range(1000, 9999 + 1):
        print("Error: number has to be in range from 1000 to 9999.")
        return main()

    print(f"Number = {number}, second right digit = {(number % 100) // 10}")
    return 1


if __name__ == '__main__':
    main()