from typing import Any
from shapes.detect import is_rectangle, is_square, is_triangle
from shapes.calc import rectangle_perimeter, rectangle_area, square_perimeter, square_area, \
    triangle_perimeter, triangle_area

def process_shapes(shapes: list[list[float]]) -> tuple[dict[str, list[dict[str, Any]]], 
    list[list[float]]]:

    processed_shapes: dict = {
        "rectangles": [],
        "squares": [],
        "triangles": []
    }

    invalid_shapes: list[list[float]] = list()

    shape_type: str = ""
    shape_perimeter = 0.0
    shape_area = 0.0

    for shape in shapes:
        if is_rectangle(shape):
            shape_type = "rectangles"
            shape_perimeter = rectangle_perimeter(shape)
            shape_area = rectangle_area(shape)

        elif is_square(shape):
            shape_type = "squares"
            shape_perimeter = square_perimeter(shape)
            shape_area = square_area(shape)

        elif is_triangle(shape):
            shape_type = "triangles"
            shape_perimeter = triangle_perimeter(shape)
            shape_area = triangle_area(shape)

        else:
            invalid_shapes.append(shape)
            continue

        for processed_shape in processed_shapes[shape_type]:
            if processed_shape["sides"] == shape:
                continue

        processed_shapes[shape_type].append({
            "sides": shape,
            "area": shape_area,
            "perimeter": shape_perimeter
        })

    return processed_shapes, invalid_shapes