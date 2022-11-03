def main():
    number = int(input("Enter number: "))
    temp = 0

    while temp <= number:
        if temp % 2 == 0 and temp != 0:
            print(temp)

        temp += 2

    return 1


if __name__ == '__main__':
    main()