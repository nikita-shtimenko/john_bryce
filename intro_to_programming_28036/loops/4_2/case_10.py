def main():
    number = int(input("Enter number: "))
    number_str = str(number)
    print(f"Left digit: {int(number_str[0])}")
    return 1


if __name__ == '__main__':
    main()