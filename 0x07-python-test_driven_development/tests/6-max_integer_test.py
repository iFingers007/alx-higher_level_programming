#!/usr/bin/python3

""" unittest for max integer function



"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest test cases for maximum integer within a list
    """

    def test_empty_list(self):
        """Test when the list is empty
        """
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """When the input list is one element
        """
        self.assertEqual(max_integer([12]), 12)

    def test_positive_elements(self):
        """For positive elements of input
        """
        self.assertEqual(max_integer([3, 5, 7, 10, 4, 12]), 12)

    def test_negative_elements(self):
        """For negative elements
        """
        self.assertEqual(max_integer([-2, -5, -9, -3]), -2)

    def test_mixed_elements(self):
        """For mixed elements
        """
        self.assertEqual(max_integer([-3, 5, -2, -9, 11]), 11)

    def test_duplicate_maximum(self):
        """When the Maximum integer is duplicated
        """
        self.assertEqual(max_integer([2, 4, 9, 6, 9]), 9)
        self.assertEqual(max_integer([-3, -5, -8, -9, -1]), -1)

    def test_contains_zero(self):
        """When element contains zero
        """
        self.assertEqual(max_integer([0, 1, 5, 3, 8, 12]), 12)
        self.assertEqual(max_integer([-3, -5, -8, 0, -9]), 0)

    def test_mixed_data_types(self):
        """Test when the input list contains a mix of integers and floats.
        """
        self.assertEqual(max_integer([2, 1, 4.5, 8, 2]), 8)
        self.assertEqual(max_integer([-5, -1, -9.5, -8]), -1)

    def test_float_data_type(self):
        """Test when the input list contains only floating-point numbers.
        """
        self.assertEqual(max_integer([3.5, 4.2, 8.5, 8.7, 7.6]), 8.7)
        self.assertEqual(max_integer([-3.7, -8.9, -2.1, -5.2, -1.5]), -1.5)

    def test_non_integer_elements(self):
        """Test when the input list contains non-integer elements (TypeError).
        """
        with self.assertRaises(TypeError):
            max_integer([1, 2, '3', 8, 2])
        with self.assertRaises(TypeError):
            max_integer([2.5, '3.6', 5.4])
        with self.assertRaises(TypeError):
            max_integer([2, None, 5])
        with self.assertRaises(TypeError):
            max_integer([2.5, 3.6, None, 5.4])


if __name__=='__main__':
    unittest.main()
