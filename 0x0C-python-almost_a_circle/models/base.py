#!/usr/bin/python3
"""Module with class Base"""


class Base:
    """ Class as the base of all other classes
    Manages if attribute in all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
