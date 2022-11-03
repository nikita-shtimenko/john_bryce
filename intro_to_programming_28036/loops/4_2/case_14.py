def main():
    number = int(input("Enter number: "))
    number_str = str(number)

    print(int(number_str[::-1]))
    return 1


if __name__ == '__main__':
    main()