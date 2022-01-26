#!/usr/bin/python3
class LockedClass:
    """A locked class that prevents the user from dinamically creating new instance attributes,
    except if the new instance attribute is called 'first_name'"""
    def __setattr__(self, name, value):
        if name == "first_name":
            self.__dict__[name] = value
        else:
            raise AttributeError("'LockedClass' object has no attribute '" + name + "'")
