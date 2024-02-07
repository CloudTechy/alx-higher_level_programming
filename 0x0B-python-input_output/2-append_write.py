#!/usr/bin/python3
""" Module that appends text to a file """


def append_write(filename="", text=""):
    """ appends to a file and returns character count

        Args:
            filename (str): name of file
            text(str): content to write
        Returns:
            int: no of character
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
