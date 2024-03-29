#!/usr/bin/python3

def safe_print_division(a, b):
    """Prints the division of a by b."""
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
    return (result)
