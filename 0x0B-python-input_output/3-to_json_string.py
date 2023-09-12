#!/usr/bin/python3
"""Module with function that returns JSON representation"""
import json


def to_json_string(my_obj):
    """
    Function that returns JSON representation of an object (string)
    """
    return json.dumps(my_obj)
