#!/usr/bin/python3
"""
Defines a class Rectangle
"""

class Rectangle:
    """Represents a rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """getter for the private instance att. width"""
        return self.__width
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("with must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attrib height"""
        return self.__height
    @height.setter
    def height(self, value):
        """setter for the private instance attrib height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

