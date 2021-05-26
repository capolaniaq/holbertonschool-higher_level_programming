#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Class that check a differents cases of success and failures
    with a different test, with de unittest
    """

    def test_max_inlist(self):
        """Function that check a cases with a different integers, float,
        and only number inside of the list
        """
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2.3, 5.4, -1]), 5.4)
        self.assertEqual(max_integer([1, 2, -3, -4]), 2)
        self.assertEqual(max_integer([1]), 1)

    def test_max_is_void(self):
        """Function that check a diferent cases of the arguments void
        """
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

    def test_max_in_char_str(self):
        """Function that check a case with string and words
        """
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')
        self.assertEqual(max_integer("Holberton     "), "t")
        self.assertEqual(max_integer(['a', 'hello', 'b', 'world']), 'world')

    def test_values(self):
        """FUnction that check typeError cases
        """
        with self.assertRaises(TypeError):
            max_integer([1, '2', 3, '4'])
        with self.assertRaises(TypeError):
            max_integer(2, 3, 4)
        with self.assertRaises(TypeError):
            max_integer({1, 2, 3})
