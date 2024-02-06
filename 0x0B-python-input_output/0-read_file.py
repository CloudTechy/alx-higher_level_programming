#!/usr/bin/python3
""" Module that reads a file """


def read_file(filename=""):
    """ reads a file and prints to stdout

        Args:
            filename (str): name of file
    """

    with open(filename, r, encoding="utf-8") as f:
        print(f.read())
