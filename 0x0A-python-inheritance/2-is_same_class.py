#!/usr/bin/python3
"""Module with function that tests if an object 
is an instance of the specified class"""


def is_same_class(obj, a_class):
    """Function that returns True if obj is exactly an
    instance of the specified class, otherwise False"""
    return isinstance(obj, a_class)
