def main():
    values = (0, 1, 1, 2, 3, 3, 4, 5, 6, 6, 7, 7)
    result = getSequenceUniqueValues(values)
    
    print(result)
    return 1

def getSequenceUniqueValues(values: tuple) -> tuple:
    return tuple(i for i in values if values.count(i) == 1)

if __name__ == '__main__':
    main()