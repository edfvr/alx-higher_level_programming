#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A Square class"""

    def __init__(self, size=0):
        """Square class initialized with size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return self.__size**2
