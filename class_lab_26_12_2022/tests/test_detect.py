from shapes.detect import is_rectangle, is_square, is_triangle

def test_detect_rectangle_empty():
    rectangle = []
    return_value = is_rectangle(rectangle)

    assert not return_value, "Error: empty sides list"

def test_detect_rectangle_negative():
    rectangle = [2.0, 0.0, -1.0, 2.0]
    return_value = is_rectangle(rectangle)

    assert not return_value, "Error: can not build a reactangle with side <= 0.0"

def test_detect_rectangle_invalid():
    rectangle = [2.0, 3.0, 4.0, 5.0]
    return_value = is_rectangle(rectangle)

    assert not return_value, "Error: invalid sides, not a rectangle"

def test_detect_square_empty():
    square = []
    return_value = is_square(square)

    assert not return_value, "Error: empty sides list"

def test_detect_square_negative():
    square = [0.0, -1.0, 0.0, 0.0]
    return_value = is_square(square)

    assert not return_value, "Error: can not build a square with side <= 0.0"

def test_detect_square_invalid():
    square = [2.0, 3.0, 4.0, 5.0]
    return_value = is_square(square)

    assert not return_value, "Error: invalid sides, not a square"

def test_detect_triangle_empty():
    triangle = []
    return_value = is_triangle(triangle)

    assert not return_value, "Error: empty sides list"

def test_detect_triangle_negative():
    triangle = [3, 0.0, -1.0]
    return_value = is_triangle(triangle)

    assert not return_value, "Error: can not build a triangle with side <= 0.0"

def test_detect_triangle_invalid():
    triangle = []
    return_value = is_triangle(triangle)

    assert not return_value, "Error: invalid sides, not a triangle"