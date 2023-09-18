#!/usr/bin/python3
"""Module with class MyList"""


class MyList(list):
    """Class that inherits from list"""

    def print_sorted(self):
        """Function that prints list in ascending order"""
        print(sorted(self))
