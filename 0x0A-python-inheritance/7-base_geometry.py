#!/usr/bin/python3
'''
Class has two function, area(self) and
integer_validator(self, name, value)
'''


class BaseGeometry:
    '''
    This is an empty class
    '''
    def area(self):
        '''
        This is a public function for area
        Raises:
            Exception: area() is not implemented
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
        This is a public function

        Args:
            name: which is a string
            value: which must be an int

        Raises:
            TypeError: <name> must be an integer
            ValueError: <name> must be greater than 0
        '''
        self.name = name
        self.value = value
        if type(self.value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        if self.value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
