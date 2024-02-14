#!/usr/bin/python3
""" Base of all classess in the models """


class Base:
    """Defines the base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the base class

            args:
                self (object) : instance of base class
                id (int): integer number
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
