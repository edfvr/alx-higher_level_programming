#!/usr/bin/python3
"""Creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """Creates an Object from JSON file"""
    with open(filename, 'r') as file:
        return json.loads(file.read())
