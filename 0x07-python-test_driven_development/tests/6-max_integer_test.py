#!/usr/bin/python3

""" Test cases for 6-max_integer_test """

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    """ test for all cases on max_integer """

    def test_max_integer(self):

        res = max_integer([2, 4, 3])
        self.assertEqual(res, 4)

    def test_max_at_end(self):

        self.assertEqual(max_integer([1, 3, 4]), 4)

    def test_max_at_start(self):

        self.assertEqual(max_integer([5, 3, 4]), 5)

    def test_with_negative(self):

        self.assertEqual(max_integer([-1, 3, 4]), 4)

    def test_single_list(self):

        self.assertEqual(max_integer([4]), 4)

    def test_negative_list(self):

        self.assertEqual(max_integer([-1, -3, -4]), -1)

    def test_empty_list(self):

        self.assertEqual(max_integer([]), None)
