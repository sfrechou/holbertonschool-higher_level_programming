#!/usr/bin/python3
"""Module for task 5 - Save Object to file"""
import json


def save_to_json_file(my_obj, filename):
    """Write obj to file using JSON"""
    with open(filename, mode='w') as my_file:
        return my_file.write(json.dumps(my_obj))
