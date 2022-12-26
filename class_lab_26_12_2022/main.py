from tests.test_detect import test_detect_rectangle_empty, test_detect_rectangle_invalid, \
    test_detect_rectangle_negative, test_detect_square_empty, test_detect_square_invalid, \
    test_detect_square_negative, test_detect_triangle_empty, test_detect_triangle_invalid, \
    test_detect_triangle_negative

from tests.test_calc import test_calc_rectangle_area, test_calc_rectangle_perimeter, \
    test_calc_square_area, test_calc_square_perimeter, test_calc_triangle_area, \
    test_calc_triangle_perimeter

from tests.test_complex import test_complex_process_shapes

def main():
    print(">>>>> Run test for module: test_detect.py")

    test_detect_rectangle_empty()
    print("test_detect.py: test_detect_rectangle_empty - PASSED")
    test_detect_rectangle_invalid()
    print("test_detect.py: test_detect_rectangle_invalid - PASSED")
    test_detect_rectangle_negative()
    print("test_detect.py: test_detect_rectangle_negative - PASSED")

    test_detect_square_empty()
    print("test_detect.py: test_detect_square_empty - PASSED")
    test_detect_square_invalid()
    print("test_detect.py: test_detect_square_invalid - PASSED")
    test_detect_square_negative()
    print("test_detect.py: test_detect_square_negative - PASSED")

    test_detect_triangle_empty()
    print("test_detect.py: test_detect_triangle_empty - PASSED")
    test_detect_triangle_invalid()
    print("test_detect.py: test_detect_triangle_invalid - PASSED")
    test_detect_triangle_negative()
    print("test_detect.py: test_detect_triangle_negative - PASSED")

    print(">>>>> Run test for module: test_calc.py")

    test_calc_rectangle_area()
    print("test_calc.py: test_calc_rectangle_area - PASSED")
    test_calc_rectangle_perimeter()
    print("test_calc.py: test_calc_rectangle_perimeter - PASSED")
    test_calc_square_area()
    print("test_calc.py: test_calc_square_area - PASSED")
    test_calc_square_perimeter()
    print("test_calc.py: test_calc_square_perimeter - PASSED")
    test_calc_triangle_area()
    print("test_calc.py: test_calc_triangle_area - PASSED")
    test_calc_triangle_perimeter()
    print("test_calc.py: test_calc_triangle_perimeter - PASSED")

    print(">>>>> Run test for module: test_complex.py")

    test_complex_process_shapes()
    print("test_complex.py: test_complex_process_shapes - PASSED")

if __name__ == '__main__':
    main()