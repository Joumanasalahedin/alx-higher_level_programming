#!/usr/bin/python3
""" Module with function that writes an object to a text file """
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    using a JSON representative """
    with open(filename, 'w', encoding="utf-8") as file:
        json_rep = json.dumps(my_obj)
        file.write(json_rep)
