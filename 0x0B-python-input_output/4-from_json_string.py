#!/usr/bin/python3

""" Module that loads a json """


import json


def from_json_string(my_str):
    """ deserialize my_str

        Args:
            my_str (str): str to deserialize
        Returns:
            object: dict
    """
    return (json.loads(my_str))
