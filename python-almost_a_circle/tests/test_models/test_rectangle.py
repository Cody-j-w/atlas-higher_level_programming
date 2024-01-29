#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from io import StringIO
import sys


class TestRectangleAttributes(unittest.TestCase):
    def test_rectangle_str_width(self):
        with self.assertRaises(TypeError):
            bad_rect = Rectangle("two", 2)

    def test_rectangle_str_height(self):
        with self.assertRaises(TypeError):
            bad_rect = Rectangle(2, "two")

    def test_rectangle_str_x(self):
        with self.assertRaises(TypeError):
            bad_rect = Rectangle(2, 2, "two")

    def test_rectangle_str_y(self):
        with self.assertRaises(TypeError):
            bad_rect = Rectangle(2, 2, 2, "two")

    def test_rectangle_neg_width(self):
        with self.assertRaises(ValueError):
            bad_rect = Rectangle(-2, 2)

    def test_rectangle_zero_width(self):
        with self.assertRaises(ValueError):
            bad_rect = Rectangle(0, 2)

    def test_rectangle_neg_height(self):
        with self.assertRaises(ValueError):
            bad_rect = Rectangle(2, -2)

    def test_rectangle_zero_height(self):
        with self.assertRaises(ValueError):
            bad_rect = Rectangle(2, 0)

    def test_rectangle_neg_x(self):
        with self.assertRaises(ValueError):
            bad_rect = Rectangle(2, 2, -2)

    def test_rectangle_neg_y(self):
        with self.assertRaises(ValueError):
            bad_rect = Rectangle(2, 2, 2, -2)

    def test_custom_id(self):
        new_rectangle = Rectangle(10, 10, 2, 2, 15)
        self.assertEqual(new_rectangle.width, 10)
        self.assertEqual(new_rectangle.height, 10)
        self.assertEqual(new_rectangle.x, 2)
        self.assertEqual(new_rectangle.y, 2)
        self.assertEqual(new_rectangle.id, 15)

    def test_area(self):
        area_rect = Rectangle(5, 5)
        self.assertEqual(area_rect.area(), 25)

    def test_rect_str(self):
        str_rect = Rectangle(10, 10, 2, 2, 42)
        self.assertEqual(str_rect.__str__(), "[Rectangle] (42) 2/2 - 10/10")

class TestRectangleDisplayMethod(unittest.TestCase):

    def test_display_no_offset(self):
        dis_rect_1 = Rectangle(5, 1)
        output = StringIO()
        sys.stdout = output
        dis_rect_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "#####\n")

    def test_display_x_offset(self):
        dis_rect_1 = Rectangle(5, 1, 2)
        output = StringIO()
        sys.stdout = output
        dis_rect_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "  #####\n")

    def test_display_offset(self):
        dis_rect_1 = Rectangle(5, 1, 2, 2)
        output = StringIO()
        sys.stdout = output
        dis_rect_1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(output.getvalue(), "\n\n  #####\n")

class TestRectangleUpdateMethod(unittest.TestCase):
    def test_args_update(self):
        new_rectangle = Rectangle(10, 10, 2, 2, 15)
        self.assertEqual(new_rectangle.id, 15)
        new_rectangle.update(72, 5, 5, 4, 4)
        self.assertEqual(new_rectangle.id, 72)
        self.assertEqual(new_rectangle.width, 5)
        self.assertEqual(new_rectangle.height, 5)
        self.assertEqual(new_rectangle.x, 4)
        self.assertEqual(new_rectangle.y, 4)

    def test_kwargs_update(self):
        update_dict = {'id': 105, 'width': 20, 'height': 20, 'x': 2, 'y': 2}
        new_rectangle = Rectangle(2, 2, 0, 0, 10)
        new_rectangle.update(**update_dict)
        self.assertEqual(new_rectangle.id, 105)
        self.assertEqual(new_rectangle.width, 20)
        self.assertEqual(new_rectangle.height, 20)
        self.assertEqual(new_rectangle.x, 2)
        self.assertEqual(new_rectangle.y, 2)