def main():
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))

    if first_val > second_val:
        print(second_val, first_val)
    else:
        print(first_val, second_val)
        
    return 1


if __name__ == '__main__':
    main()