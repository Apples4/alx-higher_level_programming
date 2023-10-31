#!/usr/bin/python3
'''
This module '5-text_indentation.py' has one function text_indentation(text)
'''


def text_indentation(text):
    '''
    Args:
        text is a string input

    Return:
         prints a text with 2 new lines after ., ? and :

    Raises:
        TypeError: text must be a string
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    end_line = 0
    for i in text:
        if end_line == 0:
            if i == ' ':
                continue
            else:
                end_line = 1
        if end_line == 1:
            if i == '?' or i == '.' or i == ':':
                print(i)
                print()
                end_line = 0
            else:
                print(i, end="")
