#!/usr/bin/python3
'''
Class that defines a rectangle
'''


class Rectangle:

    def __init__(self, width=0, height=0):
        ''' init function '''
        self.__height = 0
        self.__width = 0
        self.width = width
        self.height = height

    @property
    def height(self):
        ''' getter function for height'''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter function for height'''
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        ''' getter function for width'''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter function for width'''
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        ''' area function '''
        return self.__width * self.__height

    def perimeter(self):
        ''' parameter function '''
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * (self.__width + self.__height))
