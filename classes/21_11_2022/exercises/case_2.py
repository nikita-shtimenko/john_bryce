def main():
    numbers = (2, 4, 6)
    result = getMultiplyOfNumbersSequence(numbers)
    
    print(result)
    return 1

def getMultiplyOfNumbersSequence(numbers: tuple) -> float:
    if not numbers: # empty tuple
        return 0.0

    result = 1.0

    for i in numbers:
        result *= i

    return float(result)

if __name__ == '__main__':
    main()