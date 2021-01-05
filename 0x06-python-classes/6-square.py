#!/usr/bin/python3
"""class Square that defines a square"""


class Square:
    """class Square that defines a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optional size and position"""
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """property to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter to set it"""
        if type(value) is int:
            if value >= 0:
                self.__size = value
            else:
                raise ValueError("size must be >= 0")
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """property to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """property setter to set it"""
        if type(value) is tuple and len(value) is 2:
            if all(elements > 0 for elements in value):
                self.__position = value

    def area(self):
        """Public instance method that returns the current square area"""
        return self.__size * self.__size

    def my_print(self):
        """Public instance method that prints the square with the char #"""
        if self.__size > 0:
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
