#!/usr/bin/python3

""" Module for is kind class



"""


def is_kind_of_class(obj, a_class):
    """To add two numbers

    parameters:
    a (int) = The first number
    b (int) = The second number

    Returns:
    int: result of the addition

    Raises:
    TypeError: If number is not an integer or float
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
