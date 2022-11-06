def main():
    number = 0
    digits = None

    while True:
        try:
            number = int(input("Enter a number: "))
        except ValueError:
            print("Error: you have to enter a number.")
            continue

        if number < 0:
            break

        digits = list(map(int, str(number)))
        print(sum(digits))
            
    return 1


if __name__ == '__main__':
    main()