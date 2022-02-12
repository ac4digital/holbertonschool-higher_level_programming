#!/usr/bin/python3
"""Define a Class Retangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter, validations"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter, validations"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter, validations"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter, validations"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public Method that returns
        the area value of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Adding the public method that prints
        the Rectangle with the character #
        """
        for e in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()
