#!/usr/bin/python3
"""Defines a Python class-to-JsON object function."""


def class_to_json(obj):
    """Return the dictionary represntation of a class."""
    return obj.__dict__
