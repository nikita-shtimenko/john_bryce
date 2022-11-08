first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number % second_number == 0:
    print(f"{first_number} % {second_number} == 0")
elif second_number % first_number == 0:
    print(f"{second_number} % {first_number} == 0")
else:
    print("None")