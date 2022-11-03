def main():
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))

    if first_val > second_val:
        print(first_val)
    else:
        print(second_val)

    return 1


if __name__ == '__main__':
    main()