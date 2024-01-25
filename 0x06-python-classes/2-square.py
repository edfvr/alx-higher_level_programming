class Square:
    """Square class represents a geometric square.

    Attributes:
        __size (int): The size of the square.

    Methods:
       init__(elf, s):Initializes a new __size  instance of the Square class.
    """

    def __init__(self, size=0):
        """Initializes a new instance of the Square class.

        Args:
            size (int): The size of the square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
