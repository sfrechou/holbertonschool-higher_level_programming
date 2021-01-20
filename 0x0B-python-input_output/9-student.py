#!/usr/bin/python3
"""Module for task 8 - Class to JSON"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation for Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """retrieve dictionary"""
        return self.__dict__
