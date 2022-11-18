"""
    Option 1
    Using nested loop
"""
number = int(input("Enter a number: "))

for i in range(1, number + 1):
    output = ""
    for j in range(0, i):
        output += str(i)

    print(output)

"""
    Option 2
    Using single loop
"""
number = int(input("Enter a number: "))

for i in range(1, number + 1):
    print(str(i) * i)