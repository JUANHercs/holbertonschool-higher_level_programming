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
        self.__y = 0
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
            raise("width must be >= 0")
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
            raise TypeError("height must be integer")
        if value <= 0:
            raise ValueError("height must be >= 0")
            self.__height = value

    @property
    def x(self):
        """Set/get the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set/get the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")
