def main():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))

    print(f"Perimeter: {2 * (length + width)}")
    print(f"Square area: {length * width}")
    return 1


if __name__ == '__main__':
    main()