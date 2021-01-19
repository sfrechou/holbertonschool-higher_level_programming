#!/usr/bin/python3
"""
Module for task 4.
"""


def inherits_from(obj, a_class):
    """checks if object is exact instance of class"""
    if issubclass(a_class, type(obj)):
        return False
    else:
        return True
