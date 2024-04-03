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
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        """ Public instance that returns
        area
        """
        product = (self.size) * (self.size)
        return product
    def my_print(self):
        """ Public instance that
        prints #
        """
        if self.size == 0:
            print()
        else:
            result = self.area()
            for i in range(int(result/self.size)):
                for j in range(int(result/self.size)):
                    print("#", end="")
                print()
        
