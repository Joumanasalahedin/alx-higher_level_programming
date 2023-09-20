#!/usr/bin/python3
"""Module for test Rectangle class"""
from io import StringIO
import sys
import unittest
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """ Suite to test Rectangle class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_new_rectangle(self):
        """ Test new rectangle """
        new = Rectangle(1, 1)
        self.assertEqual(new.width, 1)
        self.assertEqual(new.height, 1)
        self.assertEqual(new.x, 0)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 1)

    def test_new_rectangle2(self):
        """ Test new rectangle """
        new = Rectangle(5, 4, 3, 0, 18)
        self.assertEqual(new.width, 5)
        self.assertEqual(new.height, 4)
        self.assertEqual(new.x, 3)
        self.assertEqual(new.y, 0)
        self.assertEqual(new.id, 18)

    def test_wrong_number_attrs(self):
        """ Test error raised with wrong number of args """
        with self.assertRaises(TypeError):
            new = Rectangle()
        with self.assertRaises(TypeError):
            new = Rectangle(5)

    def test_area(self):
        """ Checking the return value of area method """
        new = Rectangle(10, 5)
        self.assertEqual(new.area(), 50)
        new1 = Rectangle(5, 3)
        self.assertEqual(new1.area(), 15)

    def test_display_3(self):
        """ Test string printed """
        r1 = Rectangle(5, 4, 1, 1)
        res = "\n #####\n #####\n #####\n #####\n"
        with patch('sys.stdout', new=StringIO()) as str_out:
            r1.display()
            self.assertEqual(str_out.getvalue(), res)
