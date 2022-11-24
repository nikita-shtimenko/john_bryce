def main():
    number = 12
    result = mySqrt(number)

    print(number, result)
    return 1

def mySqrt(number: int) -> int:
    """
        Newton's (Newton-Rapson) method
        https://en.wikipedia.org/wiki/Newton%27s_method
    """
    
    root = number / 2

    while abs(root * root - number) >= 0.1:
        root -= (root * root - number) / (number * 2)

    return int(root)

if __name__ == '__main__':
    main()