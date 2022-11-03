def main():
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))

    if first_val % second_val == 0:
        print(f"{first_val} % {second_val} == 0")
    elif second_val % first_val == 0:
        print(f"{second_val} % {first_val} == 0")
    else:
        print("None")
        
    return 1


if __name__ == '__main__':
    main()