def main():
    num_max = int(input("Enter max number: "))
    num_den = int(input("Enter den number: "))
    temp = 0

    while temp <= num_max:
        if temp != 0 and (temp % num_den == 0):
            print(temp)

        temp += 1

    return 1


if __name__ == '__main__':
    main()