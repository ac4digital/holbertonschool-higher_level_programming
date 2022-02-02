#!/usr/bin/python3
"""
Contains the class BaseGeometry
"""


def add_attribute(obj, name, value):
    """Adds a new attribute if is possible"""
    types = (int, float, complex, set, dict, tuple, list, bool, frozenset, type, object, str)
    for _type in types:
        if type(obj) is _type:
            raise TypeError("can't add new attribute")
    object.__setattr__(obj, name, value)
