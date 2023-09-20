#!/usr/bin/python3
"""Module for test Base class"""
import io
import sys
import unittest
from models.base import Base


class TestBaseMethods(unittest.TestCase):
    """ Suite to test Base class """

    def setUp(self):
        """ Method invoked for each test """
        Base._Base__nb_objects = 0

    def test_id(self):
        """ Test assigned id """
        new = Base(1)
        self.assertEqual(new.id, 1)

    def test_id_default(self):
        """ Test default id """
        new = Base()
        self.assertEqual(new.id, 1)

    def test_id_mix(self):
        """ Test nb object attributes and assigned id """
        new = Base()
        new2 = Base(700)
        new3 = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(new2.id, 700)
        self.assertEqual(new3.id, 2)
