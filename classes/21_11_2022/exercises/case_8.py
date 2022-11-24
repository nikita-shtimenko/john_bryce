def main():
    value = 51
    result = isPrimeNumber(value)
    
    print(result)
    return 1

def isPrimeNumber(number: int) -> bool:
    if number <= 1:
        return False
    
    for i in range(1, number + 1):
        if number % i != 0:
            continue

        if i not in [1, number]:
            return False
    
    return True

if __name__ == '__main__':
    main()