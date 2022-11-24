def main():
    values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    printSequenceEvenNumbers(values)
    return 1

def printSequenceEvenNumbers(values: tuple) -> bool:
    if not values:
        return False
    
    for i in values:
        if i % 2 == 0:
            print(i)
    
    return True

if __name__ == '__main__':s
    main()