#!/usr/bin/python3
"""Checks if the object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Function that determins if the object is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False
