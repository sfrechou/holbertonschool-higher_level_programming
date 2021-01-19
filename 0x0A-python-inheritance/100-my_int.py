#!/usr/bin/python3
"""
Module for task 12.
"""


class MyInt(int):
    """Class MyInt"""
    def __eq__(self, num):
        """Class MyInt"""
        return False

    def __ne__(self, num):
        """Class MyInt"""
        return True
