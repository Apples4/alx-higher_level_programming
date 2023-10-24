#!/usr/bin/python3
"""Defining a class Square to print squares based on position and area"""


class Square:
    ''' defining the methodes in class '''
    def __init__(self, size=0, position=(0, 0)):
        ''' init the square class
            parameter size is type int
            parameter position is type int '''
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """ getter function to get the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter function """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """ getter function for position """
        return self.__position

    @position.setter
    def position(self, value):
        """ setter function for position """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(element, int) for element in value) or
                not all(element >= 0 for element in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    ''' public instance '''
    def area(self):
        ''' Method to calculate the area '''
        return(self.__size * self.__size)

    def my_print(self):
        ''' Method to print the area and posistion '''
        if self.__size == 0:
            print("")

        print("\n" * self.__position[1], end="")
        for i in range(0, self.__size):
            print(" " * self.__position[0], end="")
            for j in range(0, self.__size):
                print("#", end="")
            print("")
