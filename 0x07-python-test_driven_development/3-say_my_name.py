#!/usr/bin/python3

""" Prints out names """


def say_my_name(first_name, last_name=""):
    """ Prints out first name and the last name

    args:
        first_name (string): first name
        second_name (strinf): last name

    Returns:
        (NULL) Prints: My name is <first name> <last name>
    """
    if first_name == "":
        raise ValueError("first_name must not be empty")

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f'My name is {first_name} {last_name}')
