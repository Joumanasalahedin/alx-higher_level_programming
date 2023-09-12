#!/usr/bin/python3
""" Module with function that returns an object
representated by a JSON string """
import json


def from_json_string(my_str):
    """
    Function that returns an object (Python data structure)
    representated by a JSON string """
    return json.loads(my_str)
