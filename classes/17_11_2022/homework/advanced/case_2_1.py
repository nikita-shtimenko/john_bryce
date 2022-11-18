number = int(input("Enter a number: "))
spaces = number - 1

print("\r")

# rows
for i in range(0, number):

    # setup spaces for each row
    for j in range(0, spaces):
        print(end=" ")

    spaces -= 1

    # columns
    for j in range(0, i + 1):
        print("* ", end="")

    print("\r")