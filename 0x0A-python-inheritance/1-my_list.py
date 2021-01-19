#!/usr/bin/python3
"""
Module for task 1.
"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """ list available attributes of object"""
        # Make a copy of the list so as to not edit the original
        # Use self because of inheritance.
        new = self[:]
        new.sort()
        print("{}".format(new))
