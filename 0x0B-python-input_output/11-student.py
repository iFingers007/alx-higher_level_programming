#!/usr/bin/python3

""" Module for JSON representation
"""


class Student:
    """ defines a student class """
    def __init__(self, first_name, last_name, age):
        """ Defines instnt attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns the dictionary description with simple data structure

        Args:
        attrs: atrributes

        Returns:
        dictionary description
        """
        if attrs is None:
            return self.__dict__
        return {atr: getattr(self, atr) for atr in attrs if hasattr(self, atr)}

    def reload_from_json(self, json):
        """replaces all atributes of the student instance"""
        for key, value in json.items():
            setattr(self, key, value)
