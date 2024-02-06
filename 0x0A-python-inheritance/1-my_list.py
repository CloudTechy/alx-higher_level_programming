#!/usr/bin/python3
""" sorts list """


class MyList(list):
    """ A class List """

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """ prints sorted list """

        print(sorted(self))
