#!/usr/bin/python3
"""
Module for task 1. Real definition of a rectangle
"""


class Rectangle:
    """Class that defines a Rectangle"""

    def __init__(self, width=0, height=0):
        """Instantiation attributes"""
        self.__width = width
        self.__height = height

    @property
    def height(self):
        """Property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """Property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
