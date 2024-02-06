#!/usr/bin/python3
"""Appends string to end of text file"""


def append_write(filename="", text=""):
    """Appends string to end of text file and
    return the number of characters added"""

    with open(filename, mode='a') as file:
        number_char = file.write(text)
        return number_char
