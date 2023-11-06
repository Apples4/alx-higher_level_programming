#!/usr/bin/python3

'''
This function that returns a sorted list
'''


def lookup(obj):
    '''
    Args:
        obj: the object input

    Return:
        list of available attributes and methods of an object

    Raises:
        None
    '''
    return (list(dir(obj)))
