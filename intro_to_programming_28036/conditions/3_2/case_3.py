def main():
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))
    third_val = int(input("Enter third value: "))

    if first_val > second_val and first_val > third_val:
        print(first_val)
    elif second_val > first_val and second_val > third_val:
        print(second_val)
    elif third_val > first_val and third_val > second_val:
        print(third_val)
    elif first_val == second_val or first_val == third_val:
        print(first_val)
    elif second_val == third_val:
        print(second_val)
        
    return 1


if __name__ == '__main__':
    main()