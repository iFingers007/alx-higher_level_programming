#!/usr/bin/python3

""" Module for appends function
"""


def append_write(filename="", text=""):
    """ Appends a string at the end of a text file

    Args:
    filename: Filename of document
    text: text to be written

    """
    with open(filename, "a", encoding="utf-8") as fileAppend:
        return fileAppend.write(text)
