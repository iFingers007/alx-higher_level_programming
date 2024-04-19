#!/usr/bin/python3
"""Square subclass"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The square subclass of Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialisation function of the subclass"""
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        """String rep of Square subclass"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    @property
    def size(self):
        """Gets the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """Sets size of the square"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ For updating using unknown args"""
        if args:
            attr = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attr[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Dictionary representation of square subclass"""
        return {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
