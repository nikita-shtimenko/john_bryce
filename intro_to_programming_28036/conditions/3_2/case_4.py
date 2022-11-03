def main():
    number = int(input("Enter number (1 - 9999): "))

    if number >= 1 and number < 10:
        print("1")
    elif number >= 10 and number < 100:
        print("2")
    elif number >= 100 and number < 1000:
        print("3")
    elif number >= 1000 and number < 9999:
        print("4")
        
    return 1


if __name__ == '__main__':
    main()