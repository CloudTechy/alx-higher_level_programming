#!/usr/bin/python3
"""Defines a Rectangle subclass for  Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square class."""

    def __init__(self, size):
        """Initialize a new square class.

        Args:
            size (int): The size of square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the str() representation of a Rectangle."""
        string = "[" + str(self.__class__.__name__) + "] "
        string += str(self.__width) + "/" + str(self.__height)
        return string
