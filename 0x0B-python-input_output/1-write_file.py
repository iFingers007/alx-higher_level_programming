#!/usr/bin/python3

""" Module for write function
"""


def write_file(filename="", text=""):
    """ writes a string to a text file

    Args:
    filename: Filename of document
    text: text to be written

    """
    with open(filename, "w", encoding="utf-8") as fileWrite:
        return fileWrite.write(text)
