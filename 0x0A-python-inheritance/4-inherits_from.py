#!/usr/bin/python3

""" Module for inherit from



"""


def inherits_from(obj, a_class):
    """Checks if an object inherits

    parameters:
    obj: Object to be checked
    a_class: class to be compared to

    Returns:
    bool: True or false

    """
    if issubclass(obj, a_class):
        return True
    else:
        return False
