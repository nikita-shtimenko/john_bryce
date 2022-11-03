def main():
    number = int(input("Enter number: "))
    print(f"Next even number: {(number + 2) - (number % 2)}")
    return 1


if __name__ == '__main__':
    main()