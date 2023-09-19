#!/usr/bin/python3
"""Module for class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""

    def __init__(self, size):
        """Initializes instance"""
        Rectangle.__init__(self, size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Returns square area"""
        return self.__size ** 2
