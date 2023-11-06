#!/usr/bin/python3

'''
This class MyList is for printing a list
'''


class MyList(list):
    '''
    Represent a list
    '''
    def print_sorted(self):
        '''
        Args:
            list: that is inherited from class

        Return:
            list that is sorted

        Raises:
            None
        '''
        return(print(sorted(self, reverse=False)))
