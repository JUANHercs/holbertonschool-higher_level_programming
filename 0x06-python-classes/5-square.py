#!/usr/bin/python3
""" defines a square """


class Square:
    """ square class"""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """ docorator getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """ Decorator setter"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0 ")
        self.__size = value

    def area(self):
        """ square area"""
        area = self.__size ** 2
        return area

    def my_print(self):
        """ suqare print """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            for j in range(self.__size):
                print('#', end="")
            print()
