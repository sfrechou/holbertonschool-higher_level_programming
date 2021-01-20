#!/usr/bin/python3
"""Module for task 10 - Student to JSON with filter"""


class Student:
    """Class Student"""
    def __init__(self, first_name, last_name, age):
        """Instantiation for Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieve dictionary"""
        my_dict = {}
        if attrs is not None:
            for i in attrs:
                if type(i) is str:
                    if i in self.__dict__:
                        my_dict[i] = self.__dict__[i]
            return my_dict
        else:
            return self.__dict__
