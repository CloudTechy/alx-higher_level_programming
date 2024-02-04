#!/usr/bin/python3

""" Module that prints 2 lines after some character """


def text_indentation(text):
    """ prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text(str): text to break into 2 lines
    Returns:
        (NONE): prints out broken texts
    """

    if not text:
        return
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buf = text.split(".")
    main = ".\n\n".join([x.strip() for x in buf])
    buf = main.split("?")
    main = "?\n\n".join([x.strip() for x in buf])
    buf = main.split(":")
    main = ":\n\n".join([x.strip() for x in buf])

    print(main.strip("\n"), end="")
