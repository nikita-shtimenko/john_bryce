def main():
    number = int(input("Enter 3-digit number (from 100 to 999): "))

    if number not in range(100, 999 + 1):
        print("Error: number has to be in range from 100 to 999.")
        return main()
        
    print(f"Number = {number}, hunders digit = {number // 100}")
    return 1


if __name__ == '__main__':
    main()