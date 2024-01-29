#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square"""

    def __init__(self, size=0):
        """Square initialized with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise valueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size**2
