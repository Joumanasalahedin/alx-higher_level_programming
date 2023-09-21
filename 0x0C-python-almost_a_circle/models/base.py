#!/usr/bin/python3
"""Module with class Base"""
import json
import csv


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

        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = f"{cls.__name__}.json"

        try:
            with open(filename, 'r', encoding="utf-8") as file:
                content = file.read()

            list_cls = cls.from_json_string(content)
            instances = []
            for i in range(len(list_cls)):
                instances.append(cls.create(**list_cls[i]))

            return instances

        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves object in CSV file"""
        filename = f"{cls.__name__}.csv"

        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)

            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow(
                        [obj.id, obj.width, obj.height, obj.x, obj.y])
                if cls.__name__ == "Square":
                    writer.writerow(
                        [obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """Loads instances from CSV file"""
        filename = f"{cls.__name__}.csv"
        objects = []

        with open(filename, 'r', newline="") as file:
            reader = csv.reader(file)
            for line in reader:
                if cls.__name__ == "Rectangle":
                    list_cls = {"id": int(line[0]),
                                "width": int(line[1]),
                                "height": int(line[2]),
                                "x": int(line[3]),
                                "y": int(line[4])}
                if cls.__name__ == "Square":
                    list_cls = {"id": int(line[0]),
                                "size": int(line[1]),
                                "x": int(line[2]),
                                "y": int(line[3])}

                content = cls.create(**list_cls)
                objects.append(content)

        return objects
