#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    Square class.

    Attributes:
    __size (int): Size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize square.

        Args:
            size (int, optional): Size of the square.
         Defaults to 0.

         Raises:
            TypeError: If size is not integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2
