#!/usr/bin/python3
""" Module that prints a square with '#' """


def print_square(size):
    """
    Function prints a square with '#' character
    Args:
    size (int): size of square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        for _ in range(size):
            print("#", end='')
        print('')
