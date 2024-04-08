#!/usr/bin/python3

""" Module for the rectangle class
    and its method


"""


class Rectangle:
    """ A rectangle class """

    def __init__(self, width=0, height=0):
        """ Initialization of Rectangle class objects

        Args:
        width (int): Width of rectangle
        height (int): Height of rectangle

        Raises:
        ValueError: If width is less than 0
        TypeError: If width is not an integer
        """

        self.width = width
        self.height = height

        @property
        def width(self):
            """ For getting the width of the triangle """

            return self.__width

        @width.setter
        def width(self, value):
            """ For setting the width of the triangle """


            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """ For getting the height of the triangle """

            return self.__height

        @height.setter
        def height(self, value):
            """ For setting the height of the triangle """

            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
