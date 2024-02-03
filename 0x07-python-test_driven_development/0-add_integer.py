#!/usr/bin/python3

def add_integer(a, b=98):
    """ adds two numbers

    args:

        a (int or float): integer or float number
        b (int or float): integer or float number

    Returns:
        int: returns the sum of a and b
    """

    if not isinstance(a, int) and not isinstance(a, float):
        
        raise TypeError("a must be an integer")
    
    if not isinstance(b, int) and not isinstance(b, float):

        raise TypeError("b must be an integer")
    return int(a) + int(b)
