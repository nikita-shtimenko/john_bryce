first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

if first_number > second_number and first_number > third_number:
    print(first_number)
    if second_number > third_number:
        print(second_number)
        print(third_number)
    else:
        print(third_number)
        print(second_number)

elif second_number > first_number and second_number > third_number:
    print(second_number)
    if first_number > third_number:
        print(first_number)
        print(third_number)
    else:
        print(third_number)
        print(first_number)

elif third_number > first_number and third_number > second_number:
    print(third_number)
    if first_number > second_number:
        print(first_number)
        print(second_number)
    else:
        print(second_number)
        print(first_number)
        