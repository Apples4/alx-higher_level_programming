#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
'''
This class inherits from superclass Rectangle, multilevel inheritance
'''


class Square(Rectangle):
    '''
    The class has one function
    '''
    def __init__(self, size):
        '''
        Args:
            size: the int size of square
        '''
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
        self.area()
