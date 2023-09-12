#!/usr/bin/python3
""" Module with function that appends a string to a text file """


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file

    Returns: number of characters
    """
    with open(filename, 'a', encoding="utf-8") as file:
        return file.write(text)
