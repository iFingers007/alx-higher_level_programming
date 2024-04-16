#!/usr/bin/python3
import json
""" Module for JSON representation
"""


def to_json_string(my_obj):
    """ Returns the JSON representation of an object (string)

    Args:
    Object argument passed

    Returns:JSON representation
    """

    return json.dumps(my_obj)
