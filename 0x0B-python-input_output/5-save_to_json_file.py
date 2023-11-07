#!/usr/bin/python3
'''
function that save python
file into JSON
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Args:
        my_obj- the content I want to save
        filename- the file being converted

    Return:
        JSON file
    '''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
