#!/usr/bin/python3

""" Prints a block of # to form square """


def print_square(size):
    """ prints a square with the character #

    arg:
        size (int) : size of square
    Returns:
        (NULL) :  prints a square with #
    """

    if not size:
        return 
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    if size > 1:
        for i in range(size):
            print("#" * size)
