#!/usr/bin/python3

""" Module for JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
    my_obj: object argument
    filename: filename of text file

    """
    with open(filename, "w") as fileWrite:
        json.dump(my_obj, fileWrite)
