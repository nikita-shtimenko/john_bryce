def main():
    printPascalsTriangle(10)
    return 1

def printPascalsTriangle(rows_count: int) -> bool:
    if rows_count <= 0:
        print("")
        return False

    for row in range(rows_count):
        # set spaces for each row (make it look like a triangle)
        print(' ' * (rows_count - row), end='')
        # print row
        print(' '.join(map(str, str(11 ** row))))

    return True

if __name__ == '__main__':
    main()