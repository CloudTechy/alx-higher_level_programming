#!/usr/bin/python3

""" Module that creates a json file"""


import json


def save_to_json_file(my_obj, filename):
    """ serialize my_obj and save to filename

        Args:
            my_obj (any): obj to serialize
            filename (str): name of file
    """

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
