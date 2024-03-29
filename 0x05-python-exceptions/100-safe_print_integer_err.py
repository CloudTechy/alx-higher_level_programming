#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    """Safe prints an integer.

    If a ValueError message is caught, a corresponding
    message is printed to the stderr.

    Args:
        value (int): The int value  to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
