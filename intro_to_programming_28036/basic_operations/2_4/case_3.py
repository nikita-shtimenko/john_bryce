def main():
    pot_diameter = int(input("Enter diameter: "))
    pot_depth = int(input("Enter depth: "))

    P_VALUE = 3.14

    pot_radius = pot_diameter / 2
    pot_bottom_area = (pot_radius ** 2) * P_VALUE

    pot_capacity = pot_bottom_area * pot_depth
    print(f"Pot capacity = {pot_capacity}")
    return 1


if __name__ == '__main__':
    main()