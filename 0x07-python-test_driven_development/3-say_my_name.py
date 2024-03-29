#!/usr/bin/python3
"""A function that prints a string with given first name and last name."""


def say_my_name(first_name, last_name=""):
    """Prints a string indicating the given first name and last name."""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
