#!/usr/bin/python3
"""Returns the Object representation of a JSON"""
import json


def from_json_string(my_str):
    """Returns the Object representation of a JSON"""
    return json.loads(my_str)
