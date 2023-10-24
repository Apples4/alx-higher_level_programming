#!/usr/bin/python3
'''Defining a class called Square'''


class Square:
    ''' Defining the methodes in the class '''
    def __init__(self, size=0):
        ''' Initialising variables '''
        self.__size = size

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        ''' Method that gets the area '''
        return(self.__size * self.__size)
