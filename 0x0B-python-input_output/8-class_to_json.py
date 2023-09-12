#!/usr/bin/python3
"""Module that returns the dictionary description with a simple
data structure for a JSON serialization of an object"""


def class_to_json(obj):
    """ Function that returns the description of an object (obj) """
    return obj.__dict__
