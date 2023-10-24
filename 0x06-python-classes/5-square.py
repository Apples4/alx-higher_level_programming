#!/usr/bin/python3
''' Defining class Square '''


class Square:
    ''' defining the methodes in class '''
    def __init__(self, size=0):
        ''' init the square class
            parameter size is type int '''
        self.__size = size

    ''' getter function to get the size of the square '''
    @property
    def size(self):
        return self.__size

    ''' setter function '''
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    ''' public instance '''
    def area(self):
        ''' Methode to get the area '''
        return(self.__size * self.__size)

    def my_print(self):
        ''' Methode to print the area in # '''
        if self.__size == 0:
            print("")

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print("")
