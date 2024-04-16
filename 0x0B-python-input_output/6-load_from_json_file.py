#!/usr/bin/python3

""" Module for JSON representation
"""
import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
    filename: filename of text file

    """
    with open(filename, "r") as fileWrite:
        jsonData = json.load(fileWrite)
    return jsonData
