#!/usr/bin/python3
'''
This module '4-inherits_from.py'
has one function
def inherits_from(obj, a_class)
'''


def inherits_from(obj, a_class):
    '''
    Args:
        obj: the object input
        a_class: class being verified

    Return:
        True if the object is an instance of a class
        that inherited (directly or indirectly)
        from the specified class;
        otherwise False
    Raises:
        None
    '''
    return((isinstance(obj, a_class)) and type(obj) is not a_class)
