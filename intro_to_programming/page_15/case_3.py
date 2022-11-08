pot_diameter = int(input("Enter diameter: "))
pot_depth = int(input("Enter depth: "))

pot_radius = pot_diameter / 2
pot_bottom_area = (pot_radius ** 2) * 3.14

pot_capacity = pot_bottom_area * pot_depth
print(f"Pot capacity = {pot_capacity}")