#!/usr/bin/python3
""" Module that writes to a file """


def write_file(filename="", text=""):
    """ reads a file and prints to stdout

        Args:
            filename (str): name of file
            text(str): content to write
    """

    with open(filename, w, encoding="utf-8") as f:
        return f.write(text)
