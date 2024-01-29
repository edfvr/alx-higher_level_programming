#!/usr/bin/python3
"""A class Square that defines a square"""


class Square:
    """A class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Square initialized with size"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Retrieves position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of square"""
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """prints in stdout the square with the character #"""
        if (self.__size == 0):
            print()
            return
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            val = self.__position[0]
            if val > 0:
                print(' ' * val, end="")
            for i in range(self.__size):
                print("#", end="")
            print()
