#!/usr/bin/python3
"""
define a rectangle
"""
from models.base import Base


class Rectangle(Base):
    """ this is a rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize a rctangle"""
        self.__width = width
        self.__height = height
        self.__x = 0
        self. __y = 0
        super().__init__(id)

    @property
    def width(self):
        """
        getter of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter of eidth
        """
        if type(value) is not int:
            raise TypeError("width must be integer")
        if value <= 0:
            raise("width must be grater that 0")
        self.__width = value

    @property
    def height(self):
        """
        getter of height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        set height
        """
        if type(value) is not int:
            raise TypeError("value must be integer")
        if value <= 0:
            raise ValueError("height mus be grater than 0")
            self.__height = value
