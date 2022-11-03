def main():
    number = int(input("Enter 3-digit number (from 100 to 999): "))
    print(f"Number = {number}, hunders digit = {number // 100}")
    return 1


if __name__ == '__main__':
    main()