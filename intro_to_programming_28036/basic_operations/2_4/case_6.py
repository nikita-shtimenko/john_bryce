def main():
    number = int(input("Enter number (from 1000 to 9999): "))
    print(f"Number = {number}, second right digit = {(number % 100) // 10}")
    return 1


if __name__ == '__main__':
    main()