#!/usr/bin/python3
""" checks for class instance """


def is_kind_of_class(obj, a_class):
    """ checks if the object is an instance of a class
    that inherited from, the specified class 

    Args:
        obj (any): obj to check
        a_class: class to verify with
    Returns:
        True: if the check is true else False
    """

    if isinstance(obj, a_class):
        return True
    return False
