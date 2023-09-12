#!/usr/bin/python3
def read_file(filename=""):
    """
    Function that reads from a file and prints data
    """
    with open(filename, encoding='utf-8') as file:
        read_data = file.read()
        print(read_data, end='')
