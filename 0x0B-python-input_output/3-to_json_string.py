#!/usr/bin/python3

""" Module that creates a json """


import json


def to_json_string(my_obj):
    """ serialize my_obj

        Args:
            my_obj (any): obj to serialize
        Returns:
            object: json
    """
    return (json.dumps(my_obj))
