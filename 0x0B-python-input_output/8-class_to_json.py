#!/usr/bin/python3
'''
This function returns a dictionary description
'''


def class_to_json(obj):
    '''
    Args:
        obj-a super class

    Return:
        a dictionary description
    '''
    return obj.__dict__
