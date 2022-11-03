def main():
    number = int(input("Enter number: "))
    digits = list(map(int, str(number)))

    print(f"Digits sum = {sum(digits)}")
    return 1


if __name__ == '__main__':
    main()