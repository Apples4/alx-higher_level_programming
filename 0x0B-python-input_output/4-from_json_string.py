#!/usr/bin/python3
'''
function that decodes JSON file to python file
'''
import json


def from_json_string(my_str):
    '''
    Args:
        str- input JSON string type

    Return:
        Python object format
    '''
    return json.loads(my_str)
