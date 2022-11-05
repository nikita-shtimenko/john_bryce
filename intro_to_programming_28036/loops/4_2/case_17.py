def main():
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    temp = 1
    result = first_number

    while temp < second_number:
        result *= first_number
        temp += 1
    
    print(f"Result is {result}")
    return 1


if __name__ == '__main__':
    main()