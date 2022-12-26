from shapes.complex import process_shapes

def test_complex_process_shapes():
    shapes = [
        # rectangles
        [2.0, 3.0, 2.0, 3.0], # valid
        [2.0, 3.0, 4.0, 5.0], # invalid
        [1.0, 0.0, -1.0, 0.0], # zeros/negative

        # squares
        [2.0, 2.0, 2.0, 2.0], # valid
        [2.0, 3.0, 3.0, 3.0], # invalid
        [2.0, 0.0, -1.0, 3.0], # zeros/negative

        # triangles
        [3.0, 4.0, 5.0], # valid
        [8.0, 2.0, 3.0], # invalid
        [3.0, -1.0, 0.0] # zeros/negative
    ]

    excpected_result = (
        {
            "rectangles": [
                {
                    "sides": [2.0, 3.0, 2.0, 3.0],
                    "area": 6.0,
                    "perimeter": 10.0
                }
            ],
            "squares": [
                {
                    "sides": [2.0, 2.0, 2.0, 2.0],
                    "area": 4.0,
                    "perimeter": 8.0
                }
            ],
            "triangles": [
                {
                    "sides": [3.0, 4.0, 5.0],
                    "area": 6.0,
                    "perimeter": 12.0
                }
            ]
        },
        [
            # rectangles
            [2.0, 3.0, 4.0, 5.0], # invalid
            [1.0, 0.0, -1.0, 0.0], # zeros/negative

            # squares
            [2.0, 3.0, 3.0, 3.0], # invalid
            [2.0, 0.0, -1.0, 3.0], # zeros/negative

            # triangles
            [8.0, 2.0, 3.0], # invalid
            [3.0, -1.0, 0.0] # zeros/negative
        ]
    )

    result = process_shapes(shapes)
    assert result == excpected_result, "Error: invalid result"
