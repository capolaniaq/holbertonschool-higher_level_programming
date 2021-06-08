#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_equal(self):
        b1 =  Rectangle(10, 12)
        self.assertEqual((b1.width, b1.height, b1.x, b1.y, b1.id), (10, 12, 0, 0, 1))
        b2 = Rectangle(10, 12, 1)
        self.assertEqual((b2.width, b2.height, b2.x, b2.id), (10, 12, 1, 2))
        b3 = Rectangle(10, 12, 1, 1)
        self.assertEqual((b3.width, b3.height, b3.x, b3.y, b3.id), (10, 12, 1, 1, 3))
        b4 = Rectangle(10, 12, 1, 1, 5)
        self.assertEqual((b4.width, b4.height, b4.x, b4.y, b4.id), (10, 12, 1, 1, 5))
        b5 = Rectangle(3, 2)
        self.assertEqual((b5.area()), (6))
        b6 = Rectangle(2, 10)
        self.assertEqual(b6.area(), 20)
        b7 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(b7.area(), 56)


