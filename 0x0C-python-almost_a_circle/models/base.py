#!/usr/bin/python3
"""Define a Class Base"""


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
