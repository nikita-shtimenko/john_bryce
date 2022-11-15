while True:
    number = int(input("Enter a number: "))

    if number % 2 != 0: # odd
        print("Odd number. Exit.")
        break
    
    print(number)