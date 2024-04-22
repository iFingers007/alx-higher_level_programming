#!/usr/bin/python3
"""Unit test for models/square.py"""

import io
import sys
import unittest
from models.base import Base
from models.square import Square


class TestSquare_instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the Square class."""

    def test_square_is_base(self):
        self.assertIsInstance(Square(10), Base)

    def test_square_is_Square(self):
        self.assertIsInstance(Square(10), Square)

    def test_square_is_square(self):
        self.assertIsInstance(Square(10), Square)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_arg(self):
        s1 = Square(10)
        s2 = Square(11)
        self.assertEqual(s1.id, s2.id - 1)

    def test_two_args(self):
        s1 = Square(10, 2)
        s2 = Square(2, 10)
        self.assertEqual(s1.id, s2.id - 1)

    def test_three_args(self):
        s1 = Square(2, 2, 4)
        s2 = Square(4, 4, 2)
        self.assertEqual(s1.id, s2.id - 1)

    def test_four_args(self):
        self.assertEqual(Square(1, 2, 3, 7).id, 7)

    def test_five_args(self):
        self.assertEqual(7, Square(10, 0, 0, 7).id)

    def test_more_than_five_args(self):
        with self.assertRaises(TypeError):
            Square(1, 2, 3, 4, 5, 6)

    def test_size_private(self):
        with self.assertRaises(AttributeError):
            print(Square(10, 2, 3, 4).__size)

    def test_size_getter(self):
        r = Square(5, 7, 7, 1)
        self.assertEqual(5, r.size)

    def test_size_setter(self):
        r = Square(5, 7, 7, 1)
        r.size = 10
        self.assertEqual(10, r.size)

    def test_size_getter(self):
        r = Square(5, 7, 7, 1)
        self.assertEqual(5, r.size)

    def test_width_setter(self):
        r = Square(5, 7, 7, 1)
        r.width = 10
        self.assertEqual(10, r.width)

    def test_height_getter(self):
        r = Square(5, 7, 5, 1)
        self.assertEqual(5, r.height)

    def test_height_setter(self):
        r = Square(5, 7, 5, 1)
        r.height = 10
        self.assertEqual(10, r.height)

    def test_x_getter(self):
        r = Square(5, 7, 5, 1)
        self.assertEqual(7, r.x)

    def test_x_setter(self):
        r = Square(5, 7, 7, 1)
        r.x = 10
        self.assertEqual(10, r.x)

    def test_y_getter(self):
        r = Square(5, 7, 5, 1)
        self.assertEqual(5, r.y)

    def test_y_setter(self):
        r = Square(5, 7, 5, 1)
        r.y = 10
        self.assertEqual(10, r.y)


class TestSquare_size(unittest.TestCase):
    """Unittests for testing initialization of Square size attribute."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None, 2)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid", 2)

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5, 1)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5), 2)

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3], 2)

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}), 2)

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5), 2)

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python', 2)

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'), 2)

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcedfg'), 2)

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'), 2)

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'), 2)

    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquare_x(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None, 2, 3)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid", 2, 3)

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5, 9, 3)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5), 2)

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2, 3)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True, 2, 3)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3], 2, 3)

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3}, 2, 3)

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3), 2, 3)

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}), 2, 3)

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5), 3)

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python', 2, 3)

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'), 2, 3)

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'), 2, 3)

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2, 3)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2, 1)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0, 1)


class TestSquare_y(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, None, 3)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid", 3)

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, 5.5, 3)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, complex(5), 3)

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {"a": 1, "b": 2}, 3)

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, [1, 2, 3], 1)

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, {1, 2, 3}, 1)

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, (1, 2, 3), 1)

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, frozenset({1, 2, 3, 1}), 3)

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, range(5), 3)

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, b'Python', 3)

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, bytearray(b'abcdefg'), 3)

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, memoryview(b'abcedfg'), 3)

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('inf'), 1)

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, float('nan'), 1)

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 5, -1, 0)


class TestSquare_order_of_initialization(unittest.TestCase):
    """Unittests for testing Square order of attribute initialization."""

    def test_size_before_height(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid height")

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 2, "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 2, 3, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 2, "invalid x", "invalid y")


class TestSquare_area(unittest.TestCase):
    """Unittests for testing the area method of the Square class."""

    def test_area_small(self):
        r = Square(10, 2, 0, 0)
        self.assertEqual(100, r.area())

    def test_area_large(self):
        r = Square(999999999999999, 0, 0, 1)
        self.assertAlmostEqual(999999999999998000000000000001, r.area())

    def test_area_changed_attributes(self):
        r = Square(2, 10, 1, 1)
        r.size = 7
        r.height = 14
        self.assertEqual(98, r.area())

    def test_area_one_arg(self):
        r = Square(2, 10, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)


class TestSquare_stdout(unittest.TestCase):
    """Unittests for testing __str__ and display methods of Square class."""

    @staticmethod
    def capture_stdout(rect, method):
        """Captures and returns text printed to stdout.

        Args:
            rect (Square): The Square to print to stdout.
            method (str): The method to run on rect.
        Returns:
            The text printed to stdout by calling method on sq.
        """
        capture = io.StringIO()
        sys.stdout = capture
        if method == "print":
            print(rect)
        else:
            rect.display()
        sys.stdout = sys.__stdout__
        return capture

    # Test __str__ method
    def test_str_method_print_size_height(self):
        r = Square(4, 6)
        capture = TestSquare_stdout.capture_stdout(r, "print")
        correct = "[Square] ({}) 6/0 - 4\n".format(r.id)
        self.assertEqual(correct, capture.getvalue())

    def test_str_method_size_height_x(self):
        r = Square(5, 5, 1)
        correct = "[Square] ({}) 5/1 - 5".format(r.id)
        self.assertEqual(correct, r.__str__())

    def test_str_method_size_height_x_y(self):
        r = Square(1, 8, 2, 4)
        correct = "[Square] (4) 8/2 - 1".format(r.id)
        self.assertEqual(correct, str(r))

    def test_str_method_size_height_x_y_id(self):
        r = Square(13, 2, 4, 7)
        self.assertEqual("[Square] (7) 2/4 - 13", str(r))

    def test_str_method_changed_attributes(self):
        r = Square(7, 0, 0, [4])
        r.size = 15
        r.height = 1
        r.x = 8
        r.y = 10
        self.assertEqual("[Square] ([4]) 8/10 - 15", str(r))

    def test_str_method_one_arg(self):
        r = Square(1, 3, 4, 5)
        with self.assertRaises(TypeError):
            r.__str__(1)

    # Test display method
#    def test_display_size_height(self):
#        r = Square(2, 3, 0, 0)
#        capture = TestSquare_stdout.capture_stdout(r, "display")
#        self.assertEqual("##\n##\n##\n", capture.getvalue())

#    def test_display_size_height_x(self):
#        r = Square(3, 2, 1, 1)
#        capture = TestSquare_stdout.capture_stdout(r, "display")
#        self.assertEqual(" ###\n ###\n", capture.getvalue())

#    def test_display_size_height_y(self):
#        r = Square(4, 5, 0, 0)
#        capture = TestSquare_stdout.capture_stdout(r, "display")
#        display = "\n####\n####\n####\n####\n####\n"
#        self.assertEqual(display, capture.getvalue())

#    def test_display_size_height_x_y(self):
#        r = Square(2, 4, 2, 0)
#        capture = TestSquare_stdout.capture_stdout(r, "display")
#        display = "\n\n   ##\n   ##\n   ##\n   ##\n"
#        self.assertEqual(display, capture.getvalue())

#    def test_display_one_arg(self):
#        r = Square(5, 1, 2, 4)
#        with self.assertRaises(TypeError):
#            r.display(1)


class TestSquare_update_args(unittest.TestCase):
    """Unittests for testing update args method of the Square class."""

    # Test args
    def test_update_args_zero(self):
        r = Square(10, 10, 10, 10)
        r.update()
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def test_update_args_one(self):
        r = Square(10, 10, 10, 10)
        r.update(89)
        self.assertEqual("[Square] (10) 10/10 - 89", str(r))

    def test_update_args_two(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2)
        self.assertEqual("[Square] (10) 2/10 - 89", str(r))

    def test_update_args_three(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3)
        self.assertEqual("[Square] (10) 2/3 - 89", str(r))

    def test_update_args_four(self):
        r = Square(10, 10, 10, 10)
        r.update(4, 2, 3, 89)
        self.assertEqual("[Square] (89) 2/3 - 4", str(r))

    def test_update_args_five(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 3, 4, 5)
        self.assertEqual("[Square] (4) 2/3 - 89", str(r))

    def test_update_args_more_than_five(self):
        r = Square(10, 10, 10, 10)
        r.update(2, 3, 4, 5, 6, 89)
        self.assertEqual("[Square] (5) 3/4 - 2", str(r))

    def test_update_args_None_id(self):
        r = Square(2, 4, 5, 10)
        r.update(10, 10, 10, None)
        correct = "[Square] ({}) 10/10 - 10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_None_id_and_more(self):
        r = Square(10, 10, 10, 10)
        r.update(5, 2, 3, None)
        correct = "[Square] ({}) 2/3 - 5".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_args_twice(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, 4, 5, 6)
        r.update(6, 5, 3, 2, 89)
        self.assertEqual("[Square] (2) 5/3 - 6", str(r))

    def test_update_args_invalid_size_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update("invalid", 89)

    def test_update_args_size_zero(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(0, 89)

    def test_update_args_size_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(-5, 89)

    def test_update_args_invalid_x_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(89, "invalid", 2, 3)

    def test_update_args_x_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(89, -6, 1, 2)

    def test_update_args_invalid_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, "invalid", 4)

    def test_update_args_y_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(89, 1, -6, 3)

    def test_update_args_size_before_height(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update("invalid", "invalid", 89)

    def test_update_args_size_before_x(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update("invalid", 1, "invalid", 8)

    def test_update_args_size_before_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update("invalid", 1, 2, "invalid")

    def test_update_args_x_before_y(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(89, 2, "invalid", "invalid")


class TestSquare_update_kwargs(unittest.TestCase):
    """Unittests for testing update kwargs method of the Square class."""

    def test_update_kwargs_one(self):
        r = Square(10, 10, 10, 10)
        r.update(id=1)
        self.assertEqual("[Square] (1) 10/10 - 10", str(r))

    def test_update_kwargs_two(self):
        r = Square(10, 10, 10, 10)
        r.update(size=2, id=1)
        self.assertEqual("[Square] (1) 10/10 - 2", str(r))

    def test_update_kwargs_three(self):
        r = Square(10, 10, 10, 10)
        r.update(size=2, height=3, id=89)
        self.assertEqual("[Square] (89) 10/10 - 2", str(r))

    def test_update_kwargs_four(self):
        r = Square(10, 10, 10, 10)
        r.update(id=89, x=1, y=3, size=4)
        self.assertEqual("[Square] (89) 1/3 - 4", str(r))

    def test_update_kwargs_five(self):
        r = Square(10, 10, 10, 10)
        r.update(y=5, x=8, id=99, size=1, height=2)
        self.assertEqual("[Square] (99) 8/5 - 1", str(r))

    def test_update_kwargs_None_id(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None)
        correct = "[Square] ({}) 10/10 - 10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_None_id_and_more(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None, height=7, y=9)
        correct = "[Square] ({}) 10/9 - 10".format(r.id)
        self.assertEqual(correct, str(r))

    def test_update_kwargs_twice(self):
        r = Square(10, 10, 10, 10)
        r.update(id=89, x=1, height=2)
        r.update(y=3, height=15, size=2)
        self.assertEqual("[Square] (89) 1/3 - 2", str(r))

    def test_update_kwargs_invalid_size_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(size="invalid")

    def test_update_kwargs_size_zero(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=0)

    def test_update_kwargs_size_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(size=-5)

    def test_update_kwargs_inavlid_x_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(x="invalid")

    def test_update_kwargs_x_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(x=-5)

    def test_update_kwargs_invalid_y_type(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(y="invalid")

    def test_update_kwargs_y_negative(self):
        r = Square(10, 10, 10, 10)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(y=-5)

    def test_update_args_and_kwargs(self):
        r = Square(10, 10, 10, 10)
        r.update(89, 2, height=4, y=6)
        self.assertEqual("[Square] (10) 2/10 - 89", str(r))

    def test_update_kwargs_wrong_keys(self):
        r = Square(10, 10, 10, 10)
        r.update(a=5, b=10)
        self.assertEqual("[Square] (10) 10/10 - 10", str(r))

    def test_update_kwargs_some_wrong_keys(self):
        r = Square(10, 10, 10, 10)
        r.update(height=5, id=89, a=1, b=54, x=19, y=7)
        self.assertEqual("[Square] (89) 19/7 - 10", str(r))


class TestSquare_to_dictionary(unittest.TestCase):
    """Unittests for testing to_dictionary method of the Square class."""

    def test_to_dictionary_output(self):
        r = Square(10, 2, 9, 5)
        correct = {'x': 2, 'y': 9, 'id': 5, 'size': 10}
        self.assertDictEqual(correct, r.to_dictionary())

    def test_to_dictionary_no_object_changes(self):
        r1 = Square(10, 1, 9, 5)
        r2 = Square(5, 1, 2, 10)
        r2.update(**r1.to_dictionary())
        self.assertNotEqual(r1, r2)

    def test_to_dictionary_arg(self):
        r = Square(10, 2, 4, 2)
        with self.assertRaises(TypeError):
            r.to_dictionary(1)


if __name__ == "__main__":
    unittest.main()
