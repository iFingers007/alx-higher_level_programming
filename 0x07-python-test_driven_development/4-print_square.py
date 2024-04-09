#!/usr/bin/python3

""" Module containing the funcion for printinng the charcter #



"""


def print_square(size):
    """ Prints a square with the character #

    parameters:
    size (int) = is the size length of the square


    Raises:
    TypeError: If size is not an integer, or if float is less than zero
    ValueError: If size in integer is less than Zero
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
