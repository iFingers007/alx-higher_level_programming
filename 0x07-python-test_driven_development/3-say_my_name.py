#!/usr/bin/python3

""" Module for name printing function



"""


def say_my_name(first_name, last_name=""):
    """It prints My name is <first name> <last name>

    Args:
    first_name = First name to be printed (str)
    last_name = Last name to be printed (str)

    Returns:
    String of first name and last name

    Raises:
    TypeError: If any of the name is not a string
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
