#!/usr/bin/python3

""" Module isinstance function



"""


def is_same_class(obj, a_class):
    """ Returns True if the object is exactly an instance
    of the specified class; otherwise False

    Args:
    obj = Object to be checked
    a_class = Class to checked

    Returns:
    bool: True if specified, False otherwise

    """
    return type(obj) == a_class
