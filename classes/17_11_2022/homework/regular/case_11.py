for i in range(1, 50 + 1):
    result = ""

    if i % 3 != 0 and i % 5 != 0:
        result = i

    if i % 3 == 0:
        result += "Fizz"

    if i % 5 == 0:
        result += "Buzz"

    print(result)