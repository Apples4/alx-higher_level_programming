#!/usr/bin/python3
'''
This module '3-is_kind_of_class.py'
has one function
def is_kind_of_class(obj, a_class)
'''


def is_kind_of_class(obj, a_class):
    '''
    Args:
        obj: the instance being evaluated
        a_class: the type of class

    Returns:
        True if the object is an instance of,
        or if the object is an instance of a class
        or False

    Raises:
        None
    '''
    return(isinstance(obj, a_class))
