#!/usr/bin/python3
"""class rectangle that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle by width, height, area, perimeter,
    string, repr, delete and number of instances representations"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle with optional width and height"""
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    def __str__(self):
        """Sets the print behavior of the Rectangle object."""
        rectangle = ""

        if self.__width > 0 and self.__height > 0:
            for y in range(self.__height):
                rectangle += '#' * self.__width + '\n'

        return rectangle[:-1]

    def __repr__(self):
        """Sets the repr behavior of the Rectangle object."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @property
    def width(self):
        """Get the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if type(value) is int:
            if value >= 0:
                self.__width = value
            else:
                raise TypeError("width must be >= 0")
        else:
            raise ValueError("width must be an integer")

    @property
    def height(self):
        """Get the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if type(value) is int:
            if value >= 0:
                self.__height = value
            else:
                raise TypeError("height must be >= 0")
        else:
            raise ValueError("height must be an integer")

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
