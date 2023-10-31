#!/usr/bin/python3
'''
Class that defines a rectangle
'''


class Rectangle:
    ''' this represents a rectangle '''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        ''' init function
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            ValueError: height must be >= 0
            TypeError: height must be an integer
        '''
        self.__width = width
        self.__height = height
        type(self).number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        ''' class method '''
        return (cls(size, size))

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' public function to check instance area '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if (rect_1.area() >= rect_2.area()):
            return rect_1
        else:
            return rect_2

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
        ''' public function to get area '''
        return self.__width * self.__height

    def perimeter(self):
        ''' public function to get perimeter '''
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        ''' function that prints the square '#' '''
        if (self.__width == 0 or self.__height == 0):
            return("")

        print_area = []
        for i in range(self.__height):
            [print_area.append(str(self.print_symbol))
                for j in range(self.__width)]
            if i != self.__height - 1:
                print_area.append("\n")
        return ("".join(print_area))

    def __repr__(self):
        ''' the builtin function prints details '''
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        ''' the builtin del function '''
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
