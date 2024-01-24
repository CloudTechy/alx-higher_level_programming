#!/usr/bin/python3

""" A Square class """


class Square:

    """ Defines the square """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self)
    return self.__size

    @size.setter
    def size(self, val):
        if not isinstance("int", val):
            raise TypeError(size must be an integer)
        if val < 0:
            raise ValueError(size must be >= 0)
