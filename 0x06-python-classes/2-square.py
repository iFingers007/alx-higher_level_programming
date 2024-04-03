#!/usr/bin/python3
"""Defines a class that defines Square"""


class Square:
    """A class that defines Square"""
    def __init__(self, size=0):
        """__init__ method

        Args:
        size: size of Square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
