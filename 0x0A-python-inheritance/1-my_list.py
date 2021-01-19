#!/usr/bin/python3
"""
Module for task 1.
"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """ list available attributes of object"""
        new = self[:]
        new.sort()
        print("{}".format(new))
