#!/usr/bin/python3
'''
Class has two function, area(self) and
integer_validator(self, name, value)
'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''
    class Rectangle inherits from superclass BaseGeometry
    '''

    def __init__(self, width, height):
        '''
        Args:
            width: with of rectangle
            height: height of rectangle
        '''
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
