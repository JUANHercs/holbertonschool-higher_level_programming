#!/usr/bin/python3
"""
int module

"""


class MyInt(int):
    """ inherits from int """
    def __init__(self, num):
        """ initialization value """
        self.__num = num

    def __eq__(self, other):
        """ was != is now =="""
        return int(self) != other

    def __ne__(self, other):
        """ was == now is != """
        return int(self) == other
