#!/usr/bin/python3
# function that finds a peak in a list of unsorted integers

def find_peak(list_of_integers):
    """
    Params
    list_of_integers: list of integers

    Return
    Peak integers of the unsorted list
    """
    x = list_of_integers

    if x == []:
        return None
    total = len(x)
    if total == 1:
        return x[0]
    elif total == 2:
        return max(x)
    half = int(x / 2)

    peak = x[half]
    if peak > x[half - 1] and peak > x[half + 1]:
        return peak
    elif peak < x[half - 1]:
        return output(x[:half])
    else:
        return output(x[half + 1:])
