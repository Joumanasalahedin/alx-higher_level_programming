#!/usr/bin/python3
""" Module with function that reads from a file"""


def read_file(filename=""):
    """
    Function that reads from a file and prints data
    """
    with open(filename, 'r', encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end='')
