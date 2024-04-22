#!/usr/bin/python3
"""Module for the subClass Rectangle


"""

from models.base import Base


class Rectangle(Base):
    """Rectangle subclass of the project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialisation function for the class

        Args:
        width: Rectangle width
        height: Rectangle height
        x: x cordintate
        y: cordinate
        id: Id of rectangle

        Raise:
        TypeError: When its not int
        ValueError: When args are less than zero

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Getting value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setting value of width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getting value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setting value of height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setting value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setting value of y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Computes the area of a rectangle"""
        return self.__width * self.__height

    def display(self):
        """Displays the rectangle using #"""
        for i in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """String representation of class"""
        return (f"[Rectangle] ({self.id}) "
                f"{self.x}/{self.y} - {self.width}/{self.height}")

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if len(args) != 0:
            i = 0
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.width = arg
                elif i == 2:
                    self.height = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Converts an object to a dictionary"""
        return ({
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        })
