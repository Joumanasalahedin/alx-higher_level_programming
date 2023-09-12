#!/usr/bin/python3
""" Module with function that creates an object from a JSON file"""
import json


def load_from_json_file(filename):
    """
    Function that creates an object from a JSON file
    """

    with open(filename, 'w', encoding="utf-8") as file:
        return json.load(file)
