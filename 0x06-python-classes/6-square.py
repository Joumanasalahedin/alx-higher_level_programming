#!/usr/bin/python3
"""Define a class Square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        Args:
        size (int): size of the new square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Retrieve square position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set square position"""
        if (type(value) != tuple or
                len(value) != 2 or
                type(value[0]) != int or
                type(value[1]) != int or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area"""
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print('')
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                for _ in range(self.position[0]):
                    print(" ", end='')
                for _ in range(self.size):
                    print("#", end='')
                print('')


my_square_2 = Square(3, (3, 0))
my_square_2.my_print()
