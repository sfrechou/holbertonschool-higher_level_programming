#!/usr/bin/python3
"""
Module for task 13.
"""


def add_attribute(obj, name, value):
    """add attribute when possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
