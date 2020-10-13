#!/usr/bin/python3
"""Unittests for module rectangle
"""


import unittest
import json
import pep8
import contextlib
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
    def test_pep8_rectangle(self):
        """test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0)

    def test_00_id(self):
        """test normal id of Rectangle class
            (id start in 18 because first execute the test of base)
        """
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 19)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 20)

        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

        r4 = Rectangle(10, 2, 0, 0)
        self.assertEqual(r4.id, 21)

    def test_01_get_set(self):
        """test getters and setters
        """
        r1 = Rectangle(10, 2, 1, 1)
        self.assertEqual(r1.id, 22)

        r1.width = 50
        get_w = r1.width
        r1.height = 51
        get_h = r1.height
        r1.x = 5
        get_x = r1.x
        r1.y = 5
        get_y = r1.y
        r1.id = 50000
        get_id = r1.id

        self.assertEqual(get_w, 50)
        self.assertEqual(get_h, 51)
        self.assertEqual(get_x, 5)
        self.assertEqual(get_y, 5)
        self.assertEqual(get_id, 50000)

        r1.id = None
        self.assertEqual(get_id, 50000)
        r1.id = 'naa'
        self.assertEqual(get_id, 50000)
        r1.id = float('inf')
        self.assertEqual(get_id, 50000)
        r1.id = 2.2
        self.assertEqual(get_id, 50000)

    def test_02_exception_width_height(self):
        """test raises width and height
        """
        with self.assertRaises(TypeError):
            Rectangle(2, '2')
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.width = {}
        with self.assertRaises(TypeError):
            r.width = []
        with self.assertRaises(TypeError):
            r.width = ()
        with self.assertRaises(TypeError):
            r.width = None
        with self.assertRaises(TypeError):
            r.width = float('inf')
        with self.assertRaises(TypeError):
            r.width = 2.2
        with self.assertRaises(TypeError):
            r.width = True
        with self.assertRaises(TypeError):
            r.width = -2.2
        with self.assertRaises(TypeError):
            r.width = "Hello"
        with self.assertRaises(ValueError):
            r.width = 0
        with self.assertRaises(ValueError):
            r.width = -10

        with self.assertRaises(TypeError):
            r.height = {}
        with self.assertRaises(TypeError):
            r.height = []
        with self.assertRaises(TypeError):
            r.height = ()
        with self.assertRaises(TypeError):
            r.height = None
        with self.assertRaises(TypeError):
            r.height = float('inf')
        with self.assertRaises(TypeError):
            r.height = 2.2
        with self.assertRaises(TypeError):
            r.height = True
        with self.assertRaises(TypeError):
            r.height = -2.2
        with self.assertRaises(TypeError):
            r.height = "Hello"
        with self.assertRaises(ValueError):
            r.height = 0
        with self.assertRaises(ValueError):
            r.height = -10

    def test_03_exception_x_y(self):
        """test raises x and y
        """
        r = Rectangle(10, 2)
        with self.assertRaises(TypeError):
            r.x = {}
        with self.assertRaises(TypeError):
            r.x = []
        with self.assertRaises(TypeError):
            r.x = ()
        with self.assertRaises(TypeError):
            r.x = None
        with self.assertRaises(TypeError):
            r.x = float('inf')
        with self.assertRaises(TypeError):
            r.x = 2.2
        with self.assertRaises(TypeError):
            r.x = True
        with self.assertRaises(TypeError):
            r.x = -2.2
        with self.assertRaises(TypeError):
            r.x = "Hello"
        with self.assertRaises(ValueError):
            r.x = -10
        r.x = 0
        self.assertEqual(r.x, 0)

        with self.assertRaises(TypeError):
            r.y = {}
        with self.assertRaises(TypeError):
            r.y = []
        with self.assertRaises(TypeError):
            r.y = ()
        with self.assertRaises(TypeError):
            r.y = None
        with self.assertRaises(TypeError):
            r.y = float('inf')
        with self.assertRaises(TypeError):
            r.y = 2.2
        with self.assertRaises(TypeError):
            r.y = True
        with self.assertRaises(TypeError):
            r.y = -2.2
        with self.assertRaises(TypeError):
            r.y = "Hello"
        with self.assertRaises(ValueError):
            r.y = -10
        r.y = 0
        self.assertEqual(r.y, 0)

    def test_10_area(self):
        """test the area
        """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        r1.width = 20
        self.assertEqual(r1.area(), 40)
        r1.height = 20
        self.assertEqual(r1.area(), 400)

    def test_11_area_more_args(self):
        """test area but with more arguments
        """
        r1 = Rectangle(3, 2)
        with self.assertRaises(TypeError):
            r1.area(8)
        with self.assertRaises(TypeError):
            r1.area(None)
        with self.assertRaises(TypeError):
            r1.area([], None)
        with self.assertRaises(TypeError):
            r1.area({None}, -10)

    def test_20_display(self):
        """test display normal
        """
        r1 = Rectangle(4, 6)
        expected = '####\n####\n####\n####\n####\n####\n'

        out = StringIO()
        with contextlib.redirect_stdout(out):
            r1.display()
        self.assertEqual(out.getvalue(), expected)

    def tes_21_display(self):
        """test display normal2
        """
        r2 = Rectangle(2, 2)
        expected = '##\n##\n'
        out = StringIO()
        with contextlib.redirect_stdout(out):
            r2.display()
        self.assertEqual(out.getvalue(), expected)

    def tes_22_display(self):
        """test display normal3
        """
        r2 = Rectangle(2, 2, 1, 1)
        expected = '\n ##\n ##\n'
        out = StringIO()
        with contextlib.redirect_stdout(out):
            r2.display()
        self.assertEqual(out.getvalue(), expected)

    def test_23_display(self):
        """test display normal4
        """
        r2 = Rectangle(2, 1, 3, 5)
        expected = '\n\n\n\n\n   ##\n'
        out = StringIO()
        with contextlib.redirect_stdout(out):
            r2.display()
        self.assertEqual(out.getvalue(), expected)

    def test_24_display_excep(self):
        """test display with more arguments
        """
        r2 = Rectangle(2, 1, 3, 5)
        with self.assertRaises(TypeError):
            r2.display(2)
        with self.assertRaises(TypeError):
            r2.display('asd')
        with self.assertRaises(TypeError):
            r2.display([])
        with self.assertRaises(TypeError):
            r2.display({})
        with self.assertRaises(TypeError):
            r2.display(None)

    def test_30__str__(self):
        """test __str__
        """
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

        r2 = Rectangle(5, 5, 1, 0, 29)
        self.assertEqual(r2.__str__(), '[Rectangle] (29) 1/0 - 5/5')
        with self.assertRaises(TypeError):
            print(r2.__str__('hola'))
        with self.assertRaises(TypeError):
            print(r2.__str__(5))

    def test_40_update(self):
        """test for update function
        """
        r1 = Rectangle(10, 10, 10, 10, 1000)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)
        self.assertEqual(r1.id, 1000)

        r1.update(89)
        self.assertEqual(r1.id, 89)

        r1.update(89, 2)
        self.assertEqual(r1.width, 2)

        r1.update(89, 2, 3)
        self.assertEqual(r1.height, 3)

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.x, 4)

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.y, 5)

    def test_41_update_keys(self):
        """test for update function with keys
        """
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(height=1)
        self.assertEqual(r1.height, 1)

        r1.update(width=1, x=2)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.x, 2)

        r1.update(y=1, width=2, x=3, id=89)
        self.assertEqual(r1.y, 1)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.id, 89)

        r1.update(x=1, height=2, y=3, width=4)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.y, 3)
        self.assertEqual(r1.width, 4)

    def test_42_update_more_args(self):
        """test with more arguments no keys
        """
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(1, 1, 1, 1, 1, 1, 1, 1, 1)
        r1.update(1, 1, 1, 1, 1, -1, -10, -2, -5)
        r1.update(1, 1, 1, 1, 1, [-20, 7], None, ("ss"), {})
        r1.update(1, 1, 1, 1, 1, "[-20, 7]", 'asdasd', (8), {8: 8})
        r1.update()

        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 1)
        self.assertEqual(r1.height, 1)
        self.assertEqual(r1.x, 1)
        self.assertEqual(r1.y, 1)

    def test_43_update_more_args_keys(self):
        """test more arguments with keys
        """
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(id=20, width=30, hola=78, hole=0, arroz=10)
        r1.update(ls=20, ok=30, hala=78, hilo=0, plo=10)
        r1.update(lssss=20, oasdk=30, hffala=78, hiwdlo=0, plgo=10)

        self.assertEqual(r1.id, 20)
        self.assertEqual(r1.width, 30)
        with self.assertRaises(AttributeError):
            print(r1.hola)
        with self.assertRaises(AttributeError):
            print(r1.hole)
        with self.assertRaises(AttributeError):
            print(r1.hilo)
        with self.assertRaises(AttributeError):
            print(r1.arroz)
        with self.assertRaises(AttributeError):
            print(r1.plo)

    def test_44_update_id_type(self):
        """test more types of id
        """
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(('hola'))
        self.assertEqual(r1.id, 'hola')

        r1.update([2, 3])
        self.assertEqual(r1.id, [2, 3])

        r1.update(None)
        self.assertEqual(r1.id, None)

        r1.update({8: 20, 4: 5})
        self.assertEqual(r1.id, {8: 20, 4: 5})

        r1.update(float('inf'))
        self.assertEqual(r1.id, float('inf'))

    def test_50_to_dictionary(self):
        r1 = Rectangle(10, 2, 1, 9)
        r1_dictionary = r1.to_dictionary()

        self.assertIsInstance(r1_dictionary, dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)

        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

    def test_51_to_dictionary(self):
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(id=20, width=30, hola=78, hole=0, arroz=10)
        r1.update(ls=20, ok=30, hala=78, hilo=0, plo=10)
        r1.update(lssss=20, oasdk=30, hffala=78, hiwdlo=0, plgo=10)

        r1_dictionary = r1.to_dictionary()

        self.assertIsInstance(r1_dictionary, dict)

        r2 = Rectangle(1, 1)
        r2.update(**r1_dictionary)

        self.assertNotEqual(r1, r2)
        self.assertIsNot(r1, r2)

    def test_52_to_dictionary_more_args(self):
        r1 = Rectangle(10, 2, 1, 9)
        with self.assertRaises(TypeError):
            r1_dictionary = r1.to_dictionary(78)
        with self.assertRaises(TypeError):
            r1_dictionary = r1.to_dictionary("akjs")
        with self.assertRaises(TypeError):
            r1_dictionary = r1.to_dictionary(["asdjhads", {}, (), 78])
