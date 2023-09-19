#!/usr/bin/python3
"""Module for class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square inherited from Rectangle"""

    def __init__(self, size):
        """Initializes instance"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, size, size)

    def area(self):
        """Returns square area"""
        return self.__size ** 2

    def __str__(self):
        """Returns the printable string"""
        return f"[Square] {self.__size}/{self.__size}"
