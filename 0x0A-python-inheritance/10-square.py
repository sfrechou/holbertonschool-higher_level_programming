#!/usr/bin/python3
"""
Module for task 8.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """Instantiation of Square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """Implement area"""
        return self.__size ** 2
