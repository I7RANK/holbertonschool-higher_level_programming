#!/usr/bin/python3
"""Unittests for module base
"""


import unittest
import json
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    def test_pep8_rectangle(self):
        """test pep8
        """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0)

    def test__doc__(self):
        doc_base = __import__("models").base.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.__init__.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.to_json_string.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.save_to_file.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.from_json_string.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.create.__doc__
        self.assertTrue(doc_base)

        doc_base = Base.load_from_file.__doc__
        self.assertTrue(doc_base)

    def test_ab_getid(self):
        """test exc id
            this function should go first because it adds 1 to __nb_objects.
            it damages the function below if it gets under of test_id_str
            test executes in order alphabetic
        """
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)

    def test_aa_id(self):
        """test normal id
        """
        base1 = Base()
        base2 = Base()
        base3 = Base()
        base10 = Base(12)
        basen10 = Base(-10)

        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)
        self.assertEqual(base3.id, 3)
        self.assertEqual(base10.id, 12)
        self.assertEqual(basen10.id, -10)

    def test_aa_id_str(self):
        """test str id
        """
        base4 = Base(None)
        basestr = Base("0x01")
        basehola = Base("hola")
        basec2 = Base('2')

        self.assertEqual(base4.id, 4)
        self.assertEqual(basestr.id, "0x01")
        self.assertEqual(basehola.id, "hola")
        self.assertEqual(basec2.id, '2')

    def test_aa_id_float_tf(self):
        """test floats and boolean id
        """
        base = Base(1.2)
        basen = Base(-1.2)
        basetrue = Base(True)
        basefalse = Base(False)
        basefinf = Base(float('inf'))

        self.assertEqual(base.id, 1.2)
        self.assertEqual(basen.id, -1.2)
        self.assertEqual(basetrue.id, True)
        self.assertEqual(basefalse.id, False)
        self.assertEqual(basefinf.id, float('inf'))

    def test_aa_id_struct(self):
        """test struct id
        """
        base = Base([1, 2])
        base2 = Base({1, 2})
        base3 = Base((1, 2))
        base4 = Base({'id': 12, 'name': 'hello'})
        base5 = Base([None, None])
        lis = [None, ({'id': 12, 'name': 'hello'}, [2, (2, 3)])]
        base6 = Base(lis)

        self.assertEqual(base.id, [1, 2])
        self.assertEqual(base2.id, {1, 2})
        self.assertEqual(base3.id, (1, 2))
        self.assertEqual(base4.id, {'id': 12, 'name': 'hello'})
        self.assertEqual(base5.id, [None, None])
        self.assertEqual(base6.id, lis)

    def test_aa_more_args_base(self):
        """test passing more args
        """
        with self.assertRaises(TypeError):
            Base(2, 3)
        with self.assertRaises(TypeError):
            Base([2, 3], (2, 3))
        with self.assertRaises(TypeError):
            Base(True, False, 0)
        with self.assertRaises(TypeError):
            Base([2, 3], 2.5, float('inf'), {'id': 2, 'name': 'hello'})

    def test_ab_rectangle_id(self):
        r1 = Rectangle(2, 1, 2)
        r2 = Rectangle(21, 10, 2, 1, 99)
        r3 = Rectangle(2, 5, 20)
        self.assertEqual(r1.id, 5)
        self.assertEqual(r2.id, 99)
        self.assertEqual(r3.id, 6)

    def test_ab_square_id(self):
        r1 = Square(2, 1, 2)
        r2 = Square(21, 2, 1, 20)
        r3 = Square(2, 5, 20)
        self.assertEqual(r1.id, 7)
        self.assertEqual(r2.id, 20)
        self.assertEqual(r3.id, 8)

    def test_ba_to_json_string_str(self):
        """test to_json_string function normal
        """
        true_str = '[{"id": 1, "size": 20}]'
        check = True
        json_str = Base.to_json_string([{'id': 1, 'size': 20}])
        for i in json_str:
            if i not in true_str:
                check = False

        self.assertTrue(check)
        self.assertIn('"id": 1', json_str)
        self.assertIn('"size": 20', json_str)

    def test_ba_to_json_string_vs_json_str(self):
        """test passing more args
        """
        json_str = Base.to_json_string([{'id': 1, 'size': 20}])
        json_json = json.dumps([{'id': 1, 'size': 20}])
        self.assertEqual(json_str, json_json)

        json_str = Base.to_json_string('[{"id": 1, "size": 20}]')
        str_expe = '"[{\\"id\\": 1, \\"size\\": 20}]"'
        self.assertEqual(json_str, str_expe)

    def test_ba_to_json_string_none(self):
        """test passing none
        """
        json_str = Base.to_json_string(None)
        self.assertEqual(json_str, "[]")
        json_str = Base.to_json_string([])
        self.assertEqual(json_str, "[]")
        json_str = Base.to_json_string([None])
        self.assertEqual(json_str, "[null]")

    def test_ba_to_json_string_type(self):
        """test check the type
        """
        json_str = Base.to_json_string([None])
        self.assertEqual(type(json_str), str)

        json_str = Base.to_json_string('[{"id": 1, "size": 20}]')
        self.assertEqual(type(json_str), str)

        json_str = Base.to_json_string([{'id': 1, 'size': 20}])
        json_json = json.dumps([{'id': 1, 'size': 20}])
        self.assertEqual(type(json_str), type(json_json))

    def test_ba_to_json_string_moreargs(self):
        """test passing more args
        """
        with self.assertRaises(TypeError):
            Base.to_json_string([2, 3], [{"id": 1, "size": 20}])
        with self.assertRaises(TypeError):
            Base.to_json_string('[2, 3]', '[{"id": 1, "size": 20}]')

    def test_ba_to_json_string_other_types(self):
        """test passing other types of data
        """
        json_str = Base.to_json_string(20)
        self.assertEqual(json_str, "20")

        json_str = Base.to_json_string(True)
        self.assertEqual(json_str, "true")

        json_str = Base.to_json_string(float('inf'))
        self.assertEqual(json_str, "Infinity")

        json_str = Base.to_json_string((2, 20))
        self.assertEqual(json_str, "[2, 20]")

        json_str = Base.to_json_string({20: 20, 30: 30})
        self.assertEqual(json_str, '{"20": 20, "30": 30}')

    def test_ca_from_json_string_vs_json(self):
        """test from_json_string function
        """
        json_str = Base.to_json_string([{'id': 1, 'size': 20}])
        json_loads = json.loads(json_str)
        json_base = Base.from_json_string(json_str)
        self.assertEqual(json_base, json_loads)

        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Base.to_json_string(list_input)
        list_output = Base.from_json_string(json_list_input)
        list_output_json = json.loads(json_list_input)
        self.assertEqual(list_output, list_output_json)

    def test_ca_from_json_string_more_args(self):
        """test from_json_string with more args
        """
        with self.assertRaises(TypeError):
            json_base = Base.from_json_string("[2, 3]", "[[2, 3]]")
        with self.assertRaises(TypeError):
            json_base = Base.from_json_string("[2, 3]", "[[2, 3]]", "(2, 3)")

    def test_ca_from_json_string_no_str(self):
        """test from_json_string but no pass str
        """
        with self.assertRaises(TypeError):
            json_base = Base.from_json_string(2)
        with self.assertRaises(TypeError):
            json_base = Base.from_json_string(True)
        with self.assertRaises(TypeError):
            json_base = Base.from_json_string([True, [2, 3]])

    def test_da_save_to_file_create(self):
        """test checks if it's creates the file
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            len_fl = len(file.read())

        self.assertTrue(len_fl)
        remove_files()

    def test_da_save_to_file_contend(self):
        """test checks if the contend in Rectangle.json is correct
        """
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        obj = []
        for i in [r1, r2]:
            obj.append(i.to_dictionary())
        json_str = Rectangle.to_json_string(obj)

        with open("Rectangle.json", "r") as file:
            contend_fl = file.read()

        self.assertEqual(json_str, contend_fl)

    def test_ea_create_type(self):
        """test create function
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(type(r1), type(r2))

    def test_ea_create_is_equals(self):
        """test create function
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        is_ = False
        equ = False
        if r1 is r2:
            is_ = True
        if r1 == r2:
            equ = True

        self.assertFalse(is_)
        self.assertFalse(equ)
        self.assertNotEqual(r1, r2)

    def test_ea_create_isinstance(self):
        """test checks the if is instance of Rectangle class
        """
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertIsInstance(r1, Rectangle)
        self.assertIsInstance(r2, Rectangle)

    def test_ea_create_None_and_others(self):
        """test pass None
        """
        r1_dictionary = None
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(**r1_dictionary)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(None)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create(0)
        with self.assertRaises(TypeError):
            r2 = Rectangle.create("json")
        with self.assertRaises(TypeError):
            r2 = Rectangle.create({'id': 1000, 'width': 20})


def remove_files():
    """removes Rectangle.json and Square.json file
    """
    try:
        os.remove("Square.json")
    except OSError:
        pass
    try:
        os.remove("Rectangle.json")
    except OSError:
        pass
