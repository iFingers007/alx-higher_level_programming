#!/usr/bin/python3
"""Defines a class that defines Square"""


class Square:
    """A class that defines Square"""
    def __init__(self, size=0):
        """__init__ method

        Args:
        size: size of Square
        """

        self.size = size

        @property
        def size(self):
            return self.__size
        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("Size must be an integer")
            if value < 0:
                raise ValueError("Size must be >= 0")
            self.__size = value


    def area(self):
        """ Public instance that returns
        area
        """
        product = (self.size) * (self.size)
        return product
