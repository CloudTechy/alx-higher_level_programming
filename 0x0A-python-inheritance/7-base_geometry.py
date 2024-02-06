#!/usr/bin/python3
""" A geometry class """


class BaseGeometry:
    """ A Base Geometry class """

    def area(self):
        """ solves for area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates integer value

        Args:
            name: always string
            value: integer
        """

        if not isinstance(value, int):
            raise TypeError(f'{name} must be an integer')
        if value <= 0:
            raise ValueError(f'{name} must be greater than 0')
