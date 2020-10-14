#!/usr/bin/python3
"""test to square class
"""


import unittest
import json
import pep8
import contextlib
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestSquare(unittest.TestCase):
    """test to square class
    """
    def test_pep8_rectangle(self):
        """test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0)

    def test_00_square(self):
        """test square
        """
        s1 = Square(5)
        self.assertIsInstance(s1, Square)
        self.assertEqual(s1.id, 40)
        self.assertEqual(s1.size, 5)

        s2 = Square(2, 2)
        self.assertIsInstance(s2, Square)
        self.assertEqual(s2.id, 41)
        self.assertEqual(s2.size, 2)
        self.assertEqual(s2.x, 2)

        s3 = Square(3, 1, 3)
        self.assertIsInstance(s3, Square)
        self.assertEqual(s3.id, 42)
        self.assertEqual(s3.size, 3)
        self.assertEqual(s3.x, 1)
        self.assertEqual(s3.y, 3)

    def test_01_square_display(self):
        """test display of square
        """
        r1 = Square(4)
        expected = '####\n####\n####\n####\n'

        out = StringIO()
        with contextlib.redirect_stdout(out):
            r1.display()
        self.assertEqual(out.getvalue(), expected)

        r2 = Square(2)
        expected = '##\n##\n'

        out = StringIO()
        with contextlib.redirect_stdout(out):
            r2.display()
        self.assertEqual(out.getvalue(), expected)

        r3 = Square(1)
        expected = '#\n'

        out = StringIO()
        with contextlib.redirect_stdout(out):
            r3.display()
        self.assertEqual(out.getvalue(), expected)

    def test_02_get_square(self):
        """test square getters
        """
        s1 = Square(4, 2, 2, 56)

        self.assertEqual(s1.size, 4)
        self.assertEqual(s1.x, 2)
        self.assertEqual(s1.y, 2)
        self.assertEqual(s1.id, 56)

    def test_03_set_square(self):
        """test square setters
        """
        s1 = Square(10, 10, 10, 800)

        s1.size = 2
        s1.x = 3
        s1.y = 7
        s1.id = 52
        s1.id = 588

        self.assertEqual(s1.size, 2)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 7)
        self.assertEqual(s1.id, 588)

        s1.id = 5889
        self.assertEqual(s1.id, 5889)
        s1.id = -5889
        self.assertEqual(s1.id, -5889)

    def test_03_set_square_excep(self):
        """test square setters
        """
        with self.assertRaises(TypeError):
            s1 = Square(10, 10, 10, 800, 45)
        with self.assertRaises(ValueError):
            s1 = Square(0)
        with self.assertRaises(ValueError):
            s1 = Square(10, -10, 10, 800)
        with self.assertRaises(ValueError):
            s1 = Square(10, 10, -10, 800)
        with self.assertRaises(TypeError):
            s1 = Square(10, "10", -10, 800)
        with self.assertRaises(TypeError):
            s1 = Square(10, 10, [], 800)
        with self.assertRaises(ValueError):
            s1 = Square(-10, 10, 10, 800)

    def test_10__str__(self):
        """test __str__
        """
        s1 = Square(5)
        s1.id = 50
        self.assertEqual(s1.__str__(), '[Square] (50) 0/0 - 5')

        s1.size = 10
        self.assertEqual(s1.__str__(), '[Square] (50) 0/0 - 10')
        with self.assertRaises(TypeError):
            print(s1.__str__('hola'))
        with self.assertRaises(TypeError):
            print(s1.__str__(5))

    def test_11_display(self):
        """test display
        """
        s1 = Square(2, 2, 2, 2)
        expected = '\n\n  ##\n  ##\n'

        out = StringIO()
        with contextlib.redirect_stdout(out):
            s1.display()
        self.assertEqual(out.getvalue(), expected)

        s1 = Square(3, 3, 1, 2)
        expected = '\n   ###\n   ###\n   ###\n'

        out = StringIO()
        with contextlib.redirect_stdout(out):
            s1.display()
        self.assertEqual(out.getvalue(), expected)

    def test_12_display_excep(self):
        """test exceptions
        """
        s1 = Square(2, 2, 2, 2)
        with self.assertRaises(TypeError):
            s1.display(5)
        with self.assertRaises(TypeError):
            s1.display(-5)
        with self.assertRaises(TypeError):
            s1.display("5")
        with self.assertRaises(TypeError):
            s1.display([])
        with self.assertRaises(TypeError):
            s1.display(None)

    def test_20_to_dictionary(self):
        s1 = Square(10, 2, 1, 90)
        s1_dictionary = s1.to_dictionary()

        self.assertIsInstance(s1_dictionary, dict)

        r2 = Square(1, 1)
        r2.update(**s1_dictionary)

        self.assertNotEqual(s1, r2)
        self.assertIsNot(s1, r2)

    def test_51_to_dictionary(self):
        s1 = Square(10, 10, 10, 10)

        s1.update(id=20, width=30, hola=78, hole=0, arroz=10)
        s1.update(ls=20, ok=30, hala=78, hilo=0, plo=10)
        s1.update(lssss=20, oasdk=30, hffala=78, hiwdlo=0, plgo=10)

        s1_dictionary = s1.to_dictionary()

        self.assertIsInstance(s1_dictionary, dict)

        r2 = Square(1, 1)
        r2.update(**s1_dictionary)

        self.assertNotEqual(s1, r2)
        self.assertIsNot(s1, r2)

    def test_52_to_dictionary_more_args(self):
        s1 = Square(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary(78)
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary("akjs")
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary(["asdjhads", {}, (), 78])
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary(None)
        with self.assertRaises(TypeError):
            s1_dictionary = s1.to_dictionary(-78)
