def main():
    number = int(input("Enter number: "))

    number_str = str(number)

    if number == int(number_str[::-1]):
        print("True")
    else:
        print("False")

    return 1


if __name__ == '__main__':
    main()