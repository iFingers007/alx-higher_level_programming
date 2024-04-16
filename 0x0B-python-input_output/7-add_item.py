#!/usr/bin/python3

""" Module for adding arguments to a python list
"""

import json
import sys
from os import path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    json_file = "add_item.json"
    args_list = []

    # Check if the JSON file exists
    if path.exists(json_file):
        # If it exists, load its contents into args_list
        args_list = load_from_json_file(json_file)

    # Append new arguments to the list
    args_list.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    save_to_json_file(args_list, json_file)
