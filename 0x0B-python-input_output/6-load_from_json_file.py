#!/usr/bin/python3

""" Module that creates a python obj from json file"""


import json


def load_from_json_file(filename):
    """ creates python object from deserializing filename

        Args:
            filename (str): name of json file
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
