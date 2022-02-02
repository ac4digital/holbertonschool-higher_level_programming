#!/usr/bin/python3
"""
This module checks if two objects are exactly
the same class
"""


def is_same_class(obj, a_class):
    """return true if obj is the exact class a_class, otherwise false"""
    return (type(obj) == a_class)
