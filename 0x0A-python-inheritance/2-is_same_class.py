#!/usr/bin/python3
""" contains is_same_class function. """


def is_same_class(obj, a_class):
    """ checks for instance of object
 
        args:
            obj (any): obj to check
            a_class: Class to verify from
        returns:
            True: if obj isinstance of a_class
            else False
    """
    if type(obj) == a_class:
        return True
    return False
