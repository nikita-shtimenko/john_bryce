while True:
    number = int(input("Enter a number for factorial (>= 0): "))
    
    if number < 0:
        print("Error: invalid input: number can not be < 0.")
        continue

    factorial = 1

    if number in [0, 1]:
        break

    for i in range(1, number + 1):
        factorial = factorial * i

    break

print(f"Number: {number}, factorial: {factorial}")
