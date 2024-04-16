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

    def to_json(self):
        """returns the dictionary description with simple data structure

        Args:
        obj: Object to be serialised

        Returns:
        dictionary description
        """
        attributes = self.__dict__
        ser_dict = {}

        for attrName, attrVal in attributes.items():
            if isinstance(attrVal, (list, int, dict, bool, str)):
                ser_dict[attrName] = attrVal
        return ser_dict
