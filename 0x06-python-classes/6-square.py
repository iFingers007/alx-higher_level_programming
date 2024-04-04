#!/usr/bin/python3
"""Defines a class that defines Square"""


class Square:
    """A class that defines Square"""
    def __init__(self, size=0, position=(0, 0)):
        """__init__ method

        Args:
        size: size of Square
        """

        self.size = size
        self.position = position

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

        @property
        def position(self):
            return self.__postion

        @position.setter
        def position(self, value):
            for i in value:
                if i < 0:
                    raise TypeError("position must be a tuple of 2 positive integers")
            self.__position = value

    def area(self):
        return self.size * self.size

    def my_print(self):
        for idx in range(self.position[1]):
            print()
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                space = self.position[0] * ' '
                hashes = self.size * '#'
                print(f"{space}{hashes}")
