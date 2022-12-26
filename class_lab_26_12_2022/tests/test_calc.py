from shapes.calc import rectangle_perimeter, rectangle_area, square_perimeter, square_area, \
    triangle_perimeter, triangle_area

def test_calc_rectangle_perimeter():
    rectangle = [2.0, 3.0, 2.0, 3.0]
    return_value = rectangle_perimeter(rectangle)
    print(return_value)

    assert return_value is not None, "Error: can not calculate perimeter for invalid rectangle"
    assert return_value == 10.0, "Error: invalid rectangle perimeter"

def test_calc_rectangle_area():
    rectangle = [2.0, 3.0, 2.0, 3.0]
    return_value = rectangle_area(rectangle)

    assert return_value is not None, "Error: can not calculate area for invalid rectangle"
    assert return_value == 6.0, "Error: invalid rectangle area"

def test_calc_square_perimeter():
    square = [2.0, 2.0, 2.0, 2.0]
    return_value = square_perimeter(square)

    assert return_value is not None, "Error: can not calculate perimeter for invalid square"
    assert return_value == 8.0, "Error: invalid square perimeter"

def test_calc_square_area():
    square = [2.0, 2.0, 2.0, 2.0]
    return_value = square_area(square)

    assert return_value is not None, "Error: can not calculate area for invalid square"
    assert return_value == 4.0, "Error: invalid square area"

def test_calc_triangle_perimeter():
    triangle = [3.0, 4.0, 5.0]
    return_value = triangle_perimeter(triangle)

    assert return_value is not None, "Error: can not calculate perimeter for invalid triangle"
    assert return_value == 12.0, "Error: invalid triangle perimeter"

def test_calc_triangle_area():
    triangle = [3.0, 4.0, 5.0]
    return_value = triangle_area(triangle)

    assert return_value is not None, "Error: can not calculate area for invalid triangle"
    assert return_value == 6.0, "Error: invalid triangle area"