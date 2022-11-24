def main():
    numbers = [1, 2, 3, 4, 5.1]
    result = getSumOfNumbersSequence(numbers)
    
    print(result)
    return 1

def getSumOfNumbersSequence(numbers: list) -> float:
    return float(sum(numbers))

if __name__ == '__main__':
    main()