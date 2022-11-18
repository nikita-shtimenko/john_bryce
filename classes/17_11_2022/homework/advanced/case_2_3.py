number = int(input("Enter a number: "))
spaces = 0

print("\r")

# rows
for i in range(number - 1, -1, -1):

    # setup spaces for each row
    for j in range(0, spaces):
        print(end=" ")

    spaces += 1

    # columns
    for j in range(0, i + 1):
        print("* ", end="")

    print("\r")

# update spaces (invert)
spaces = number - 1

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

print("\r")