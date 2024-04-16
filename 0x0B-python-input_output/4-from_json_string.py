#!/usr/bin/python3

""" Module for JSON representation
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string

    Args:
    my_str: String passed

    Returns: Object representation
    """

    return json.loads(my_str)
