#!/usr/bin/python3
'''
The function that save python file into a JSON file
'''
import json


def to_json_string(my_obj):
    '''
    Args:
        my_obj - input object

    Return:
        JSON representation of an object
    '''
    return json.dumps(my_obj)
