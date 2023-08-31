#!/usr/bin/python3
"""
Module consists of a function that add two integers together
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b
    Raises TypeError if a or b aren't integers or floats
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
