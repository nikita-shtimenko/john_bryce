# same as 21_11_2022/exercises/case_7.py

def main():
    value = 26
    result = isPerfectNumber(value)
    
    print(result)
    return 1

def isPerfectNumber(number: int) -> bool:
    if number <= 0:
        return False

    return number == sum([i for i in range(1, number) if number % i == 0])

if __name__ == '__main__':
    main()