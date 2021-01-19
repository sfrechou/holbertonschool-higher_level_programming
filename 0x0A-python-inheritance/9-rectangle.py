#!/usr/bin/python3
"""
Module for task 8.
"""


class BaseGeometry:
    """Base Geometry class"""

    def area(self):
        """Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validate integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """Instantiation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Implement area"""
        return self.__width * self.__height

    def __str__(self):
        """String return"""
        return "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
