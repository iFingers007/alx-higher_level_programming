#!/usr/bin/python3

""" Module for is kind class



"""


def is_kind_of_class(obj, a_class):
    """Checks if its a kind

    parameters:
    obj: Object to be checked
    a_class: Class to be compared with

    Returns:
    bool: True or false
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
