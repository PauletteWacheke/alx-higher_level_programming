#!/usr/bin/python3
""" Define a class Square"""


class Square:
    """
    Square class with private size and position attributes and methods for
    area calculation and printing

    Attributes:
        size (int): the size of the square.
        position (tuple): The position of the square.

    Methods:
        __init__(self, size=0, position=(0, 0)): Initialiazes a new
        square instance
        size(self): Getter method for size attribute.
        size(self, value): Setter method for size attribute.
        position(self): Getter method for position attribute.
        position(self, value): Setter method for position attribute.
        area(self): Calculates and returns the area of the square.
        my_print(self): Prints the square with '#' characters,
        considering the position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square. Default is 0.
            position(tuple): The position of the square.Default is (0, 0).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for size attribute.

        Returns:
            int: The size of the square.
        """

    @size.setter
    def size(self, value):
        """
        Setter method for size attribute.

        Args:
            value (int): the size to set.

        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter method for position attribute.

        Returns:
            tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for position attribute.

        Args:
            value (tuple): the position to set.

        Raises:
            TypeError: if position is not a tople of 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not
        all(isinstance((i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position=value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
            int: the area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with '#' characters, considering the position.

        If size is equal to 0, print an empty line.
        Position is used by adding spaces based on  the second
        element of the position tuple.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size
