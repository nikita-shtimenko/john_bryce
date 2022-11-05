def main():
    value = int(input("Enter number: "))
    temp = value - 1

    while temp > 0:
        if value % temp == 0:
            print(temp)

        temp -= 1
        continue
    
    return 1

if __name__ == '__main__':
    main()