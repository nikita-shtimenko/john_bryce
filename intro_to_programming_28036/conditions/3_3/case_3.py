def main():
    a = int(input("Enter A: "))
    b = int(input("Enter B: "))
    c = int(input("Enter C: "))
    d = int(input("Enter D: "))
    e = int(input("Enter E: "))
    f = int(input("Enter F: "))

    if ((a * e) - (b * d)) == 0:
        print("Eqatuion has no solution")
        return 1

    print(f"x = {((c * e) - (b * f)) / ((a * e) - (b * d))}")
    print(f"y = {((a * f) - (c * d)) / ((a * e) - (b * d))}")
    return 1


if __name__ == '__main__':
    main()