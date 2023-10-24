#!/usr/bin/python3
'''Creating a class callled Square'''


class Square:
    ''' Placing the method and field'''
    def __init__(self, size=0):
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
