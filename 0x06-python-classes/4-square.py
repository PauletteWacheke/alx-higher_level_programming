#!/usr/bin/python3
"""Define a class square"""


class Square:
    """
    Square class with private size attribute and methods for area calculation..

    Attributes:
        size (int): Size of the square.

    Methods:
        __init__(self, size=0): Initializes a new Square instance
        size(self): Getter method for size attribute.
        size(self, value): Setter method for size attribute.
        area(self): Calculates and returns the area of the square.
    """

    def __init__(self, size=0):
        """
        Initialize square.

        Args:
            size (int): the size of the square. Default is 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for size attribute.


        Returns:
            int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): The size to set.
        Raises:
            TypeError: if size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        calculates and returns the area of the square.

        Returns:
            int: The area of the sqaure.
        """
        return self.__size ** 2
