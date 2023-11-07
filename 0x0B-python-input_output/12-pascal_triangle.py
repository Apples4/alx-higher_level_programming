#!/usr/bin/python3
'''
Module that has one function
'''


def pascal_triangle(n):
    '''
    Args:
        n: input number for pascal triangele

    Return:
        Pascal triangel based on n
    '''
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row.extend([sum(pair) for pair
                    in zip(last_row, last_row[1:])])
        row.append(1)
        triangle.append(row)
    return triangle
