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
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ gets the area of a rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ Returns string representation """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """ Subclass of Rectangle """
    def __init__(self, size):
        """Initialises Square subclass"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ gets the area of a square """
        return self.__size ** 2

    def __str__(self):
        """ Returns string representation """
        return "[Square] {}/{}".format(self.__size, self.__size)
