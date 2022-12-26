from shapes.detect import is_rectangle, is_square, is_triangle

def rectangle_perimeter(sides: list[float]):
    if not is_rectangle(sides):
        return None

    side_a: float = sides[0]
    side_b: float = 0

    for side in sides:
        if side == side_a:
            continue

        side_b = side
        break

    return (side_a + side_b) * 2

def rectangle_area(sides: list[float]):
    if not is_rectangle(sides):
        return None

    side_a: float = sides[0]
    side_b: float = 0

    for side in sides:
        if side == side_a:
            continue

        side_b = side
        break

    return side_a * side_b

def square_perimeter(sides: list[float]):
    if not is_square(sides):
        return None

    return sides[0] * 4

def square_area(sides: list[float]):
    if not is_square(sides):
        return None

    return sides[0] ** 2


def triangle_perimeter(sides: list[float]):
    if not is_triangle(sides):
        return None

    return sum(sides)

def triangle_area(sides: list[float]):
    if not is_triangle(sides):
        return None

    semi_p = sum(sides) / 2
    area = (semi_p * (semi_p - sides[0]) * (semi_p - sides[1]) * (semi_p - sides[2])) ** 0.5
    return area