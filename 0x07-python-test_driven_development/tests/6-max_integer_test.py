#!/usr/bin/python3
"""Unittest for max_integer([..])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ tests for max_integer function """
    def test_max(self):
        self.assertEqual(max_integer([2, 1, 3, 4, 2, 3, 3, 3]), 4)

    def test_negatives(self):
        self.assertEqual(max_integer([-1, -2, -123456, -0]), 0)

    def test_none(self):
        self.assertEqual(max_integer([]), None)

    def test_floats(self):
        self.assertEqual(max_integer([2.5, 2.7, 2.9]), 2.9)

    def test_floats_int(self):
        self.assertEqual(max_integer([2.5, 2.7, 2.9, 6]), 6)

    def test_ope(self):
        self.assertEqual(max_integer([2 + 2, 6 * 2, 1 * 3.5]), 12)

    def test_char(self):
        self.assertEqual(max_integer(['a', 'g', 'Z']), 'g')

    def test_str(self):
        self.assertEqual(max_integer(["abc", "bca", "cba"]), "cba")
        self.assertEqual(max_integer(["zba", "bca", "czz"]), "zba")

    def test_str_int(self):
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer(["a", 2, 100]), 100)
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer(['a', 2, 100]), 100)

    def test_notlist(self):
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer({8, 2, 100}), 100)
