def is_rectangle(sides: list[float]) -> bool:
    if len(sides) != 4:
        return False

    for side in sides:
        if side <= 0.0:
            return False

        if sides.count(side) != 2:
            return False

    return True

def is_square(sides: list[float]) -> bool:
    if len(sides) != 4:
        return False

    temp: float = 0.0
    index: int = 0

    while index < len(sides):
        if temp == 0.0 and sides[index] > 0.0:
            temp = sides[index]
    
        if sides[index] != temp:
            return False

        index += 1

    return True

def is_triangle(sides: list[float]) -> bool:
    if len(sides) != 3:
        return False

    if sides[0] + sides[1] < sides[2]:
        return False

    if sides[1] + sides[2] < sides[0]:
        return False

    if sides[2] + sides[0] < sides[1]:
        return False

    return True