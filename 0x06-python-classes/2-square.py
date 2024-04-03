#!/usr/bin/python3
"""Defines a class that defines Square"""


class Square:
    """A class that defines Square"""
    def __init__(self, size):
        """__init__ method

        Args:
        size: size of Square
        """

        if not isinstance(size, int):
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("Size must be >= 0")


        self.__size = size

    def area(self):
        """ Public instance that returns
        area
        """
        product = (self.__size) *(self.__size)
        return product
