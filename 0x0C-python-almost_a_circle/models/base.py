#!/usr/bin/python3
'''
This is a fundamental file for the project
'''
import json


class Base:
    ''' class called base'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''
        Initialiser/ constructor

        Agrs:
            id which is an integer

        Return:
            An int as id or int as _nb_objects
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''
        Returns:
             the JSON string representation of list_dictionaries
        '''
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''
        writes the JSON string representation of list_objs to a file

        Args:
            list of objects of this class
        '''
        list_dict = []
        if list_objs is not None:
            for i in list_objs:
                list_dict.append(cls.to_dictionary(i))

        with open(cls.__name__ + '.json', 'w') as f:
            f.write(cls.to_json_string(list_dict))

    @staticmethod
    def from_json_string(json_string):
        '''
        Argument:
            json string type is input

        Return:
            that returns the list
        '''
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        '''
        Args:
            list of dictionaries of classes

        Return:
        '''
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        '''
        Returns:
            that returns a list of instances
        '''
        try:
            with open(cls.__name__ + '.json', 'r') as f:
                list_dictionaries = Base.from_json_string(f.read())
                return [cls.create(**dici) for dici in list_dictionaries]
        except IOError:
            return []
