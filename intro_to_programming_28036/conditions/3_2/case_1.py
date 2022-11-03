def main():
    value = int(input("Enter value: "))

    if value > 0:
        print("Positive")
    elif value < 0:
        print("Negative")
    else: # value == 0
        print("Zero")
        
    return 1


if __name__ == '__main__':
    main()