#!/usr/bin/python3

""" Test cases for 6-max_integer_test """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ test for all cases on max_integer """

    def test_max_integer(self):

        res = max_integer([2, 4, 3])
        self.assertEqual(res, 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
