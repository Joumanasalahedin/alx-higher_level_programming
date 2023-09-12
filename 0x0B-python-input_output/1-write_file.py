#!/usr/bin/python3
""" Module with function that writes a string to a text file """


def write_file(filename="", text=""):
    """
    Function that writes a string to a text file

    Returns: number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as file:
        characters = file.write(text)
        return characters
