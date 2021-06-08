#!/usr/bin/python3
""" this will be the base for all this
project
"""


class Base:
    """ base model to all the project
    classes"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialize a new base
        Args : id (int)
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
