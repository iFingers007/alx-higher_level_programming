#!/usr/bin/python3

""" Module for read function
"""


def read_file(filename=""):
    """ Reads a file and prints to stdout

    Args:
    filename: Filename of document

    """
    with open(filename, "r", encoding="utf-8") as fileRead:
        print(fileRead.read(), end='')
