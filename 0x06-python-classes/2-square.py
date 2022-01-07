#!/usr/bin/python3
"""private arg"""


class Square:
    """class square with private arg"""
    def __init__(self, size=0):
        """__init__ initialize object"""
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
