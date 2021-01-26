#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingBase(unittest.TestCase):
    """class for Test Base"""

    def test_base_repeated_id(self):
        """Base repeated ID"""
        Base._Base__nb_objects = 0
        b1 = Base()
        b2 = Base()
        b3 = Base(7)
        b4 = Base()
        b5 = Base(7)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 7)
        self.assertEqual(b4.id, 3)
        self.assertEqual(b5.id, 7)

    def test_base_types(self):
        """Base types"""
        Base._Base__nb_objects = 0
        self.assertEqual(str(type(Base)), "<class 'type'>")

        self.assertEqual(str(type(Rectangle)), "<class 'type'>")

        self.assertEqual(str(type(Square)), "<class 'type'>")

        r1 = Rectangle(2, 4)
        self.assertEqual(isinstance(r1, Rectangle), True)

        sq1 = Square(4)
        self.assertEqual(isinstance(sq1, Square), True)

        self.assertEqual(str(type(r1)), "<class 'models.rectangle.Rectangle'>")
        self.assertEqual(str(type(sq1)), "<class 'models.square.Square'>")
        self.assertEqual(issubclass(Square, Rectangle), True)
        self.assertEqual(issubclass(Square, Base), True)
        self.assertEqual(issubclass(Rectangle, Base), True)

        self.assertEqual(issubclass(Base, Rectangle), False)
        self.assertEqual(issubclass(Base, Square), False)

        r2 = Rectangle(4, 5)
        r3 = Rectangle(4, 5)
        self.assertEqual(r2 is r3, False)

        sq2 = Square(4)
        sq3 = Square(4)
        self.assertEqual(sq2 is sq3, False)

    def test_None_base(self):
        """Base empty"""
        Base._Base__nb_objects = 0
        base1 = Base(None)
        self.assertEqual(base1.id, 1)

    def test_more_args_base(self):
        """Base with more args"""
        with self.assertRaises(TypeError):
            base1 = Base(1, 2)

    # TO JSON STRING
    def test1_to_json_string(self):
        """funct to pass to JSON string"""
        Base._Base__nb_objects = 0
        rect = Rectangle(5, 4, 3, 6)
        new_dict = rect.to_dictionary()
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(new_dict, {'y': 6, 'height': 4,
                                    'width': 5, 'x': 3, 'id': 1})
        self.assertEqual(type(new_dict), dict)
        self.assertEqual(sorted(jstrg),
                         sorted('[{"height": 4, "x": 3, "width": '
                                '5, "y": 6, "id": 1}]'))
        self.assertEqual(type(jstrg), str)

    def test2_to_json_string(self):
        """funct to pass to JSON string"""
        Base._Base__nb_objects = 0
        new_dict = None
        jstrg = Base.to_json_string([new_dict])
        self.assertEqual(jstrg, '[null]')

    def test3_to_json_string(self):
        """funct to pass to JSON string"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Base.to_json_string()

        jstrg = Base.to_json_string([])
        self.assertEqual(jstrg, "[]")

        MyList = [1, 2, 3]
        jstrg = Base.to_json_string([MyList])
        self.assertEqual(jstrg, "[[1, 2, 3]]")

        with self.assertRaises(NameError):
            MyString = "Hello"
            jstrg = Base.to_json_string(MyString)
            self.assertEqual(jstrg, Hello)

        i = (1, "foo", "bar")
        jsdict = Base.to_json_string(i)
        self.assertEqual(jsdict, '[1, "foo", "bar"]')

        Rect2 = Rectangle(5, 4)
        new_dict2 = Rect2.to_dictionary()
        jstrg = Base.to_json_string([new_dict2])
        self.assertEqual(new_dict2, {'y': 0, 'height': 4,
                                     'width': 5, 'x': 0, 'id': 1})

        with self.assertRaises(TypeError):
            Rect3 = Rectangle(1)
            new_dict3 = Rect3.to_dictionary()
            jstrg2 = Base.to_json_string([new_dict3])
            Base.to_json_string(jstrg2)

    # JSON TO FILE
    def test3_json_to_file1(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        lista = [{"id": 1, "width": 2, "y": 0, "x": 0, "height": 4},
                 {"id": 2, "width": 2, "y": 0, "x": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test4_json_to_file2(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 4)
        Rectangle.save_to_file([r1])
        lista = [{"id": 1, "x": 0, "width": 2, "y": 0, "height": 4}]
        with open("Rectangle.json", "r") as file:
            file1 = file.read()
            list_output = Rectangle.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test5_json_to_file3(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        s1 = Square(4, 5)
        s2 = Square(6, 7)
        s3 = Square(8, 9)
        Square.save_to_file([s1, s2, s3])
        lista = [{"x": 5, "size": 4, "id": 1, "y": 0},
                 {"x": 7, "size": 6, "id": 2, "y": 0},
                 {"x": 9, "size": 8, "id": 3, "y": 0}]
        with open("Square.json", "r") as file:
            file1 = file.read()
            list_output = Square.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test6_json_to_file4(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        Square.save_to_file([])
        lista = []
        with open("Square.json", "r") as file:
            file1 = file.read()
            list_output = Square.from_json_string(file1)
            self.assertEqual(list_output, lista)

    def test7_json_to_file5(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            MyString = "string"
            Square.save_to_file(MyString)

    def test8_json_to_file6(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            MyNum = 13
            Square.save_to_file(MyNum)

    def test9_json_to_file7(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            MyList = ["hello", "my", "friend"]
            Square.save_to_file(MyList)

    def test10_json_to_file8(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(AttributeError):
            Square.save_to_file([None])

    def test11_json_to_file9(self):
        """ test json string into file"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            Square.save_to_file()

    # JSON STRING TO DICT
    def test_json_str_to_dic_1(self):
        """test json, str to dictionary"""
        Base._Base__nb_objects = 0
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, [{'height': 4, 'width': 10,
                                        'id': 89}, {'height': 7, 'width': 1,
                                                    'id': 7}])

    def test1_jsonstr_to_dic(self):
        """ test json to dict """
        list_input1 = [
            {'id': 97, 'width': 5, 'height': 4},
            {'id': 79, 'width': 4, 'height': 5}
        ]
        json_list_input1 = Rectangle.to_json_string(list_input1)
        list_output1 = Rectangle.from_json_string(json_list_input1)
        self.assertEqual(list_output1, [{'height': 4, 'width': 5,
                                        'id': 97}, {'height': 5, 'width': 4,
                                                    'id': 79}])

        json_list_input2 = "[]"
        list_output2 = Rectangle.from_json_string(json_list_input2)
        self.assertEqual(list_output2, [])

        json_list_input3 = None
        list_output3 = Rectangle.from_json_string(json_list_input3)
        self.assertEqual(list_output3, '[]')

        with self.assertRaises(ValueError):
            json_list_input4 = "Hello Python"
            list_output4 = Rectangle.from_json_string(json_list_input4)
            self.assertEqual(list_output4, "")

        list_input5 = [
            {'id': 97, 'width': 5}
        ]
        json_list_input5 = Rectangle.to_json_string(list_input5)
        list_output5 = Rectangle.from_json_string(json_list_input5)
        self.assertEqual(list_output5, [{'id': 97, 'width': 5}])

    # DISPLAY CON Y SIN X e Y
    def test_display_1(self):
        """test output 1"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(2, 3)
        captureOutput = io.StringIO()
        sys.stdout = captureOutput
        r1.display()
        self.assertEqual(captureOutput.getvalue(), ("##\n##\n##\n"))

        with self.assertRaises(TypeError):
            """ test output 2 """
            r2 = Rectangle()
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r2.display()

        with self.assertRaises(TypeError):
            """ test output 3 """
            r3 = Rectangle(None)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r3.display()

        with self.assertRaises(TypeError):
            """ test output 4 """
            lista = []
            r4 = Rectangle(lista)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r4.display()

        with self.assertRaises(TypeError):
            """ test output 5 """
            Base._Base__nb_objects = 0
            r5 = Rectangle(1)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r5.display()

            r6 = Square(2, 2, 2)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r6.display()
            self.assertEqual(captureOutput.getvalue(), ("\n\n##\n##\n"))

            r7 = Rectangle(2, 3, 2)
            captureOutput = io.StringIO()
            sys.stdout = captureOutput
            r7.display()
            self.assertEqual(captureOutput.getvalue(), ("\n\n##\n##\n##\n"))

    # DICTIONARY TO INSTANCE
    def test1_dict_to_inst(self):
        """ dict to instance """
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r2.__str__(), "[Rectangle] (1) 1/0 - 3/5")

        with self.assertRaises(TypeError):
            r10 = Rectangle()
            r10_dictionary = r10.to_dictionary()
            r20 = Rectangle.create(**r10_dictionary)

        with self.assertRaises(TypeError):
            r3 = Rectangle(None)
            r3_dictionary = r3.to_dictionary()
            r4 = Rectangle.create(**r3_dictionary)

        with self.assertRaises(TypeError):
            lista = []
            r5 = Rectangle.create(lista)

        with self.assertRaises(TypeError):
            r5 = Rectangle.create(2)

    # LOAD FROM FILE
    def test_load_from_file(self):
        """ load from file test """
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual([i.__dict__ for i in list_rectangles_input],
                         [i.__dict__ for i in list_rectangles_output])

if __name__ == '__main__':
    unittest.main()
