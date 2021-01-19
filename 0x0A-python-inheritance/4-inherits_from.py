#!/usr/bin/python3
"""
Module for task 4.
"""


def inherits_from(obj, a_class):
    """checks if object is exact instance of class"""
    if type(obj) == a_class:
        return False
    else:
        return isinstance(obj, a_class)
