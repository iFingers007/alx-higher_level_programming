"""
"""Module for the Class Base"""


class Base:
    """Base class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation of the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
