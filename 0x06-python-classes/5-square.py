#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
        size (int): size of the new square
        """
        self.size = size

    @property
    def size(self):
        """Retrieve square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set square size"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print('')
        else:
            for _ in range(self.size):
                for _ in range(self.size):
                    print("#", end='')
                print('')
