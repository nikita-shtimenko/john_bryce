def main():
    first_num = int(input("Enter first number: "))
    second_num = int(input("Enter second number: "))

    first_num_dividers = [i for i in range(1, first_num + 1) if first_num % i == 0]
    second_num_dividers = [i for i in range(1, second_num + 1) if second_num % i == 0]

    max_divider = 0

    for i in first_num_dividers:
        if i not in second_num_dividers:
            continue

        if i < max_divider:
            continue

        max_divider = i
    
    print(max_divider)
    return 1

if __name__ == '__main__':
    main()