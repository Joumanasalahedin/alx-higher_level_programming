#!/usr/bin/python3
"""Unittest for the function max_integer"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_max(self):
        result = max_integer([2, 5, 10])
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
