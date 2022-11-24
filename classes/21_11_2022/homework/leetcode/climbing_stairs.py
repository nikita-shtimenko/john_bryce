def main():
    number = 45
    result = climbStairs(number)

    print(number, result)
    return 1

def climbStairs(number: int) -> int:
    one, two = 1, 1

    for i in range(number - 1):
        temp = one
        one += two
        two = temp

    return one

if __name__ == '__main__':
    main()