def main():
    value = int(input("Enter first value: "))
    return [print("Even") if value % 2 == 0 else print("Odd")]


if __name__ == '__main__':
    main()