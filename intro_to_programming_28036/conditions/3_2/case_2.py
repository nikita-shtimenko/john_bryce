def main():
    first_val = int(input("Enter first value: "))
    second_val = int(input("Enter second value: "))
    third_val = int(input("Enter third value: "))

    if second_val > first_val and second_val > third_val:
        print("Increasing...")
        
    return 1


if __name__ == '__main__':
    main()