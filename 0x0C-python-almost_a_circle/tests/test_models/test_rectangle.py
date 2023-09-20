#!/usr/bin/python3
"""Module for test Rectangle class"""
import io
import sys
import unittest
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
