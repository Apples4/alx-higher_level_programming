#!/usr/bin/python3
'''
Loads info form JSON file to python file
'''
import json


def load_from_json_file(filename):
    '''
    Args:
        filename- writing from JSON file

    Return:
        Python file
    '''
    with open(filename, "r") as f:
        return json.load(f)
