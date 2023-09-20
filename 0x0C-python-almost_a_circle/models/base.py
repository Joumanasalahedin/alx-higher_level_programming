#!/usr/bin/python3
"""Module with class Base"""
import json


class Base:
    """ Class as the base of all other classes
    Manages if attribute in all classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation"""
        if list_dictionaries is None or list_dictionaries == {}:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves object in JSON file"""
        filename = f"{cls.__name__}.json"
        list_rep = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_rep.append(list_objs[i].to_dictionary())

        json_list = cls.to_json_string(list_rep)

        with open(filename, 'w', encoding="utf-8") as file:
            file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """returns list of the JSON representation"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with attricutes set"""
        if cls.__name__ == 'Rectangle':
            new = cls(5, 5)
        else:
            new = cls(5)

        new = cls.update(**dictionary)
        return new
