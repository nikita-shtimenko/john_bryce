def main():
    number = int(input("Enter 2-digit number (from 10 to 99): "))
    print(f"Number = {number}, reversed = {(number % 10)}{(number // 10)}")
    return 1


if __name__ == '__main__':
    main()