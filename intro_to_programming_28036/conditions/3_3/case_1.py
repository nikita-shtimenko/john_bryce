def main():
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))
    third_val = int(input("Enter third value: "))

    if first_val > second_val and first_val > third_val:
        print(first_val)
        if second_val > third_val:
            print(second_val)
            print(third_val)
        else:
            print(third_val)
            print(second_val)

    elif second_val > first_val and second_val > third_val:
        print(second_val)
        if first_val > third_val:
            print(first_val)
            print(third_val)
        else:
            print(third_val)
            print(first_val)

    elif third_val > first_val and third_val > second_val:
        print(third_val)
        if first_val > second_val:
            print(first_val)
            print(second_val)
        else:
            print(second_val)
            print(first_val)
            
    return 1


if __name__ == '__main__':
    main()