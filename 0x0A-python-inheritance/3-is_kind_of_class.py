#!/usr/bin/python3
"""
Module for task 3.
"""


def is_kind_of_class(obj, a_class):
    """checks if object is exact instance of class"""
    if isinstance(obj, a_class) or type(obj) == a_class:
        return True
    else:
        return False
