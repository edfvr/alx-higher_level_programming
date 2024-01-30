#!/usr/bin/python3
"""A function that adds two numbers."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.
    Otherwise raise a TypeError"""

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a+b
