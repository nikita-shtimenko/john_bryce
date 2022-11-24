def main():
    printNumbersSquare()
    return 1

def printNumbersSquare():
    return print("\n".join([f"{i ** 2}" for i in range(1, 30 + 1)]))

if __name__ == '__main__':
    main()