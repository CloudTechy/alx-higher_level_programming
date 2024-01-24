#!/usr/bin/python3

""" A Square class """


class Square:

    """ Defines the square """
    def __init__(self, size=0):
        """ Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        """ Args:
            size (int): The size of the new square.
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
