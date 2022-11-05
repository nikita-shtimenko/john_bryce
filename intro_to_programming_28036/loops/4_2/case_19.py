def main():
    number = int(input("Enter a number: "))
    result = 1

    for i in range(1, number + 1):
        result *= i
    
    print(result)
    return 1


if __name__ == '__main__':
    main()