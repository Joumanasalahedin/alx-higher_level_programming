#!/usr/bin/python3
""" Student Module """


class Student:
    """ Represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes a new student with:
        first name of the student
        last name of the student
        age of the student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Get a dictionary representation of the student
         If attrs is a list of strings, represents only those attributes
        """
        if attrs is None:
            return self.__dict__

        result = {}
        for attr in attrs:
            if type(attr) == str:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)

        return result
