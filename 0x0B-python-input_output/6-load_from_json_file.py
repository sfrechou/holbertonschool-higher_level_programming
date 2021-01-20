#!/usr/bin/python3
"""Module for task 6 - Create Object from JSON file"""
import json


def load_from_json_file(filename):
    """Create Object from JSON file"""
    with open(filename) as my_file:
        return json.load(my_file)
