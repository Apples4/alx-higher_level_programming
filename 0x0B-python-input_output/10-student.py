#!/usr/bin/python3
'''
Class that shows a dictionary representation
'''


class Student:
    '''
    class for student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Args:
            first name: string input
            last name: string input
            age: int input
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        function to get description of object

        Args:
            attrs: list of strings

        Return:
            a disctionary description
            attriutes of class
        '''
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
