#!/usr/bin/python3
"""Unittest for the function max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_max(self):
        self.assertEqual(max_integer([2, 5, 10]), 10)
        self.assertEqual(max_integer([5]), 5)

    def test_empty(self):
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        self.assertEqual(max_integer([0, -15, 25, -5, 17]), 25)
        self.assertEqual(max_integer([-5, -15, -7, -13]), -5)

    def test_type(self):
        self.assertRaises(TypeError, max_integer, 7)
