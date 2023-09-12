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

    def to_json(self):
        """ Get a dictionary representation of the student """
        return self.__dict__
