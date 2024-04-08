#!/usr/bin/python3

""" Module for the rectangle class
    and its method


"""


class Rectangle:
    """ A rectangle class """

    number_of_instances = 0
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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ For getting the width of the rectangle """

        return self.__width

    @width.setter
    def width(self, value):
        """ For setting the width of the rectangle """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ For getting the height of the rectangle """

        return self.__height

    @height.setter
    def height(self, value):
        """ For setting the height of the rectangle """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ For the area of a rectangle """

        return self.width * self.height

    def perimeter(self):
        """ To get perimeter of the rectangle """

        if self.width == 0 or self.height == 0:
            return 0
        per = 2 * (self.width + self.height)
        return per

    def __str__(self):
        """ Returns a string representation of the object """

        res = ""
        if self.width == 0 or self.height == 0:
            return ""
        return '\n'.join(["#" * self.width] * self.height)

    def __repr__(self):
        """ Returns a string that can recreate the rectangle instance """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __eval__(self):
        """ Returns a string that can recreate the rectangle instance """

        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """ Prints a message when an instance Rectangle is deleted """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
