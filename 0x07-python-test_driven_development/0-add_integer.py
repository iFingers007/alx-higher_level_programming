#!/usr/bin/python3

""" Module for add function



"""


def add_integer(a, b=98):
    """To add two numbers

    parameters:
    a (int) = The first number
    b (int) = The second number

    Returns:
    int: result of the addition

    Raises:
    TypeError: If number is not an integer or float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
