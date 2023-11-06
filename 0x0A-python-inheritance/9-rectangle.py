#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''
Class has two function, area(self) and
integer_validator(self, name, value)
'''


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

    def area(self):
        '''
        function that calculates the area

        Return:
            area of a rectangle
        '''
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
