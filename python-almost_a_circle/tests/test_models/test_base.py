#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from io import StringIO
import sys

class TestJSONStringMethod(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_non_dict(self):
        self.assertEqual(Base.to_json_string([1, 2, 3]), "[1, 2, 3]")

    def test_non_list(self):
        self.assertEqual(Base.to_json_string(42), "42")

    def test_success(self):
        rect_1 = Rectangle(4, 5)
        dict_1 = rect_1.to_dictionary()
        expected = '[{"id": 1, "width": 4, "height": 5, "x": 0, "y": 0}]'
        self.assertEqual(Base.to_json_string([dict_1]), expected)

class TestLoadFileMethod(unittest.TestCase):

class TestFromJSONMethod(unittest.TestCase):

class TestCreateMethod(unittest.TestCase):