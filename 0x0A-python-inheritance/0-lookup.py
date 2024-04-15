#!/usr/bin/python3

""" Module for look-up function



"""


def lookup(obj):
    """returns the list of available attributes and methods of an object

    parameters:
    obj = Object to be looked up

    Returns:
    list: list of available attributes and methods

    """
    return dir(obj)
