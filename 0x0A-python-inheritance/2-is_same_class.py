#!/usr/bin/python3

'''
This module '2-is_same_class.py'
has a one function
def is_same_class(obj, a_class)
'''


def is_same_class(obj, a_class):
    '''
    Args:
        obj: the object type
        that will be checked
        a_class: the suggested type of an object

    Return:
        True if correct and false if not correct

    Raises:
        None
    '''
    return type(obj) == a_class
