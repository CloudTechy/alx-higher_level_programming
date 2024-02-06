#!/usr/bin/python3
""" checks inheritance of object direct or indirectly"""


def inherits_from(obj, a_class):
    """ checks if obj is directly or indirectly
    inhetited from a_class

    Args:
        obj (any): object to check.
        a_class: class to verify from
    Returns:
        True: if check is true else False
    """

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
