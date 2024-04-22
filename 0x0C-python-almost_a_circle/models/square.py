#!/usr/bin/python3
"""Square subclass"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square subclass of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation function of the subclass"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size of the square"""
        self.width = value
        self.height = value

    def __str__(self):
        """String rep of Square subclass"""
        s1 = "[Square]"
        s2 = f"({self.id})"
        s3 = f"{self.x}/{self.y}"
        s4 = f"{self.size}"
        return s1 + ' ' + s2 + ' ' + s3 + ' - ' + s4

    def update(self, *args, **kwargs):
        """args and kwargs"""
        if len(args) != 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
                i += 1

        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """Dictionary representation of square subclass"""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        })
