#!/usr/bin/python3
import json
"""Module with function that returns JSON representation"""


def to_json_string(my_obj):
    """
    Function that returns JSON representation of an object (string)
    """
    return json.dumps(my_obj)
