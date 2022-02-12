#!/usr/bin/python3
"""Define a Class Base"""
import json


class Base:
    """
    Class Bass will be the "Base"
    of all other classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        return the JSON string representation
        of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Method that writes the JSON string
        representation of list_objs to a file
        """
        filename = cls.__name__ + '.json'
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(i.to_dictionary())
        with open(filename, "w") as f:
            f.write(cls.to_json_string(list))
