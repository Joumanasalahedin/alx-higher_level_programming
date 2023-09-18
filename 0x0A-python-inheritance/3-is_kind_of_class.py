#!/usr/bin/python3
"""Module with function that tests if object is an instance
of a class or of a class that inherited from"""


def is_kind_of_class(obj, a_class):
    """Function that returns True if obj is an instance of the specified class
    or an instance of a class that inherited from,
    otherwise False"""

    return isinstance(obj, a_class)
