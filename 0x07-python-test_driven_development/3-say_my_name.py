#!/usr/bin/python3
"""
Module that consists of a function that prints My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>
    Raises TypeError if inputs aren't strings
    """

    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
