#!/usr/bin/python3

""" Module for JSON representation
"""
import json


def class_to_json(obj):
    """returns the dictionary description with simple data structure

    Args:
    obj: Object to be serialised

    Returns:
    dictionary description
    """
    attributes = obj.__dict__
    ser_dict = {}

    for attrName, attrVal in attributes.items():
        if isinstance(attrVal, (list, int, dict, bool, str)):
            ser_dict[attrName] = attrVal
    return ser_dict
