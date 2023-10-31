#!/usr/bin/python3
'''
This module is "3-say_my_name.py"
The module has one function, say_my_name(first_name, last_name="")
'''


def say_my_name(first_name, last_name=""):
    '''
    Returns: a string that prints users name

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
