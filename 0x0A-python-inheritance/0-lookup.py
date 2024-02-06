#!/usr/bin/python3
""" prints objects attributes and methods """


def lookup(obj):
    """ gets object attr and methods

    args:
        obj(object): object
    Returns:
        (list): list of object attr and methods
    """
    return (dir(obj))
