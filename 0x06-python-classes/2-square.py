#!/usr/bin/python3
"""A class that defines a Square"""


class Square:
    """Square class represents a geometric square"""

    def __init__(self, size=0):
        """Initializes a new instance of the Square class"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
