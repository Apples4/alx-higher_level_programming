#!/usr/bin/python3
''' Unittest for function max_integer(list=[]) '''

import unittest
''' importing unittest module '''

max_integer = __import__('6-max_integer').max_integer


class Max_integer(unittest.TestCase):
    '''
    This is the class for the unittest
    '''

    def test_sorted_list(self):
        ''' function to sort the list '''
        sorted_list = [1, 2, 3, 4]
        self.assertEqual(max_integer(sorted_list), 4)

    def test_unsorted_list(self):
        ''' function to test on unsorted list '''
        unsorted_list = [4, 5, 1]
        self.assertEqual(max_integer(unsorted_list), 5)

    def test_empty_list(self):
        ''' function to test empty list '''
        e = []
        self.assertEqual(max_integer(e), None)

    def test_float(self):
        ''' function to test for max float '''
        float_test = [1.22, 3.55, 5.66, 10.11]
        self.assertEqual(max_integer(float_test), 10.11)

    def test_int_flt(self):
        ''' function to test max int and float '''
        int_flt = [1, 5, 6.2, 8.9]
        self.assertEqual(max_integer(int_flt), 8.9)

    def test_only_one(self):
        ''' function to test one element in list '''
        one_list = [2]
        self.assertEqual(max_integer(one_list), 2)

    def test_max_infront(self):
        ''' function to test max in the beginning '''
        max_infront = [10, 3, 2, 1]
        self.assertEqual(max_integer(max_infront), 10)

    def test_max_mid(self):
        ''' function to test max in the middle '''
        max_mid = [1, 100, 2]
        self.assertEqual(max_integer(max_mid), 100)

    def test_str(self):
        ''' function to test for non int input '''
        str_inp = ['a', 'b', 12]
        with self.assertRaises(TypeError):
            max_integer(str_inp)


if __name__ == "__main__":
    unittest.main()
