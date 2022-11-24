def main():
    value = 101
    result = isNumberInRange(value, 1, 100)
    
    print(result)
    return 1

def isNumberInRange(number: int, range_from: int, range_to: int) -> bool:
    return number in range(range_from, range_to + 1)

if __name__ == '__main__':
    main()