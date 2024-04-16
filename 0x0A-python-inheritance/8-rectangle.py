#!/usr/bin/python3

""" Module for Geometry class



"""


class BaseGeometry:
    """Geometry Base class
    """
    def area(self):
        """ Raises exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates the value
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """ Subclass of BaseGeometry
    """
    def __init__(self, width, height):
        """ Initialize the subclass

        Args:
        width (int): Rectangle width
        height (int): Positive height

        Raises:
        ValueError: If less than 0
        TypeError: If not an int
        """
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
