#!/usr/bin/python3
"""Square subclass"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square subclass of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation function of the subclass"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String rep of Square subclass"""
        return (f"[Square] ({self.id}) {self.__x}/{self.__y} - {self.__size}")

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size of the square"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ For updating using unknown args"""
        if args:
            n_args = len(args)
            if n_args >= 1:
                self.id = args[0] #  attr = ["id", "size", "x", "y"]
            if n_args >= 2:
                self.__size = args[1]
            if n_args >= 3:
                self.__size = args[2]
            if n_args >= 4:
                self.__x = args[3]
            if n_args >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.__size = v
                if k == 'x':
                    self.__x = v
                if k == 'y':
                    self.__y = v

    def to_dictionary(self):
        """Dictionary representation of square subclass"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
