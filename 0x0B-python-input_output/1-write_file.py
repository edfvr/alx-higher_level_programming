#!/usr/bin/python3
"""Write string to text file"""


def write_file(filename="", text=""):
    """Write string to a text file and 
    return the number of characters written"""
    with open(filename, mode='w') as file:
        number_char = file.write(text)
        return number_char
