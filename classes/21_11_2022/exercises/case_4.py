def main():
    result = getFactorialOfNumber(888)
    print(result)
    return 1

def getFactorialOfNumber(number: int) -> int:
    if number < 0:
        return 0

    if number in [0, 1]:
        return 1

    factorial = 1

    for i in range(1, number + 1):
        factorial = factorial * i

    return factorial

if __name__ == '__main__':
    main()