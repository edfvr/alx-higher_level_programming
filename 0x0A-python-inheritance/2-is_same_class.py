#!/usr/bin/python3
"""Checks if the object is an instance of a class"""


def is_same_class(obj, a_class):
    """Function that determines if the object
    is an exact instance of a_class"""
    if type(obj) is a_class:
        return True
    return False
