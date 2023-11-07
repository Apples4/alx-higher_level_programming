#!/usr/bin/python3
'''
This function writes a string to a text
'''


def write_file(filename="", text=""):
    '''
    Args:
        filename: input file to be written
        text: the strings to be written to the filename

    Return:
        number of characters written
    '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
