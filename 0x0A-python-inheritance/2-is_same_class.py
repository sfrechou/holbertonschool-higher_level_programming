#!/usr/bin/python3
"""
Module for task 2.
"""


def is_same_class(obj, a_class):
    """checks if object is exact instance of class"""
    if isinstance(obj, a_class) and type(obj) == a_class:
        return True
    else:
        return False
