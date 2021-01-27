#!/usr/bin/python3
"""Unittest for Square class
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingSquare(unittest.TestCase):
    """class for Test Square"""

    # SQUARE SIZE
    def test_square_size_string(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s1 = Square("hello")

    def test_square_size_list(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s2 = Square([9, 6])

    def test_square_size_tuple(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s3 = Square((7, 3))

    def test_square_size_dictionary(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s4 = Square({'k': 8})

    def test_square_size_zero(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            s5 = Square(0)

    def test_square_size_negative(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            s6 = Square(-7)

    def test_square_size_float(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s7 = Square(4.5)

    def test_square_size_nan(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s8 = Square(float('NaN'))

    def test_square_size_inf(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s9 = Square(float('inf'))

    def test_square_size_boolean(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s10 = Square(True)

    def test_square_size_many_args(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s11 = Square(1, 2, 3, 4, 5, 6)

    def test_square_size_empty(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s12 = Square()

    def test_square_size_impossible(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s13 = Square(5j)

    def test_square_size_big_num(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s14 = Square(1e100)

    def test_square_size_none(self):
        """Testing Square Size"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s14 = Square(None)

    # SQUARE X
    def test_square_x_string(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s1 = Square(2, "hello")

    def test_square_x_list(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s2 = Square(2, [9, 6])

    def test_square_x_tuple(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s3 = Square(4, (7, 3))

    def test_square_x_dictionary(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s4 = Square(4, {'k': 8})

    def test_square_x_negative(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            s5 = Square(6, -7)

    def test_square_x_float(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s6 = Square(2, 4.5)

    def test_square_x_nan(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s7 = Square(4, float('NaN'))

    def test_square_x_inf(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s8 = Square(6, float('inf'))

    def test_square_x_boolean(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s9 = Square(4, True)

    def test_square_x_many_args(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s10 = Square(1, 2, 3, 4, 5, 6)

    def test_square_x_zero(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        s11 = Square(9, 0)
        self.assertEqual(s11.x, 0)

    def test_square_x_impossible(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s12 = Square(2, 5j)

    def test_square_x_big(self):
        """Testing Square X"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s13 = Square(2, 1e100)

    # SQUARE Y
    def test_square_y_string(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s1 = Square(2, 3, "hello")

    def test_square_y_list(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s2 = Square(2, 3, [9, 6])

    def test_square_y_tuple(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s3 = Square(4, 3, (7, 3))

    def test_square_y_dictionary(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s4 = Square(4, 3, {'k': 8})

    def test_square_y_negative(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            s5 = Square(6, 3, -7)

    def test_square_y_float(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s6 = Square(2, 3, 4.5)

    def test_square_y_nan(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s7 = Square(4, 3, float('NaN'))

    def test_square_y_inf(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s8 = Square(6, 3, float('inf'))

    def test_square_y_boolean(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s9 = Square(4, 3, True)

    def test_square_y_many_args(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s10 = Square(1, 2, 3, 4, 5, 6)

    def test_square_y_zero(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        s11 = Square(9, 3, 0)
        self.assertEqual(s11.y, 0)

    def test_square_y_impossible(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s12 = Square(2, 2, 5j)

    def test_square_y_big(self):
        """Testing Square Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            s13 = Square(2, 3, 1e100)

    # SQUARE AREA
    def test_areaSquare(self):
        """Test area Square"""
        Base._Base__nb_objects = 0
        sq = Square(4, 4)
        self.assertEqual(sq.area(), 16)

    # SQUARE REASSIGN
    def test1_reassign_x(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        rect = Square(1, 2, 3, 4)
        rect.x = 1
        self.assertEqual(rect.x, 1)

    def test6_reassign_size(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        rect1 = Square(1, 2, 3, 4)
        rect1.size = 5
        self.assertEqual(rect1.size, 5)

    def test6_reassign_negative(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect2 = Square(1, 2, 3, 4)
            rect2.size = -1

    def test6_reassign_string(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect3 = Square(1, 2, 3, 4)
            rect3.size = "hello"

    def test6_reassign_list(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect4 = Square(1, 2, 3, 4)
            rect4.size = [9, 6]

    def test6_reassign_tuple(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect5 = Square(1, 2, 3, 4)
            rect5.y = (7, 3)

    def test6_reassign_dictionary(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect6 = Square(1, 2, 3, 4)
            rect6.size = {'k': 8}

    def test6_reassign_zero_size(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect7 = Square(1, 2, 3, 4)
            rect7.size = 0

    def test6_reassign_zero_x(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        rect1 = Square(1, 2, 3, 4)
        rect1.x = 0
        self.assertEqual(rect1.x, 0)

    def test6_reassign_float(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect8 = Square(1, 2, 3, 4)
            rect8.size = 4.5

    def test6_reassign_nan(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect8 = Square(1, 2, 3, 4)
            rect8.size = float('NaN')

    def test6_reassign_inf(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect9 = Square(1, 2, 3, 4)
            rect9.size = float('inf')

    def test6_reassign_boolean(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect9 = Square(1, 2, 3, 4)
            rect9.x = True

    def test6_reassign_impossible(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect10 = Square(1, 2, 3, 4)
            rect10.x = 5j

    def test6_reassign_big(self):
        """Square test reasign values"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect11 = Square(1, 2, 3, 4)
            rect11.y = 1e100

    # SQUARE TO DICTIONARY
    def test1_Sq_todict(self):
        """Square test to_dictionary 1"""
        Base._Base__nb_objects = 0
        sq = Square(1, 2, 3, 4)
        sq1 = sq.to_dictionary()
        MyDict = {'id': 4, 'size': 1, 'x': 2, 'y': 3}
        for i in MyDict:
            self.assertEqual(sq1[i], MyDict[i])

    def test2_Sq_todict(self):
        """Square test to_dictionary 2"""
        Base._Base__nb_objects = 0
        sq = Square(1)
        sq1 = sq.to_dictionary()
        MyDict = {'id': 1, 'size': 1, 'x': 0, 'y': 0}
        for i in MyDict:
            self.assertEqual(sq1[i], MyDict[i])

    def test3_Sq_todict(self):
        """Square test to_dictionary 3"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square()
            sq1 = sq.to_dictionary()

    def test4_Sq_todict(self):
        """Square test to_dictionary 4"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq = Square(None)
            sq1 = sq.to_dictionary()

    # SQUARE STR
    def test_str_Square1(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq1 = Square()
            sq1 = str(self)

    def test_str_Square2(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        sq2 = Square(1)
        self.assertEqual(str(sq2), "[Square] (1) 0/0 - 1")

    def test_str_Square3(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        sq3 = Square(1, 2)
        self.assertEqual(str(sq3), "[Square] (1) 2/0 - 1")

    def test_str_Square4(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        sq4 = Square(1, 2, 3)
        self.assertEqual(str(sq4), "[Square] (1) 2/3 - 1")

    def test_str_Square5(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        sq5 = Square(1, 2, 3, 4)
        self.assertEqual(str(sq5), "[Square] (4) 2/3 - 1")

    def test_str_Square6(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq6 = Square(1, 2, 3, 4, 5)
            sq6 = str(self)

    def test_str_Square7(self):
        """Test str for Square"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq7 = Square(None)
            sq7 = str(self)

    # SQUARE UPDATE
    def test_Square_update1(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq1 = Square(7, 7, 7, 7)
        self.assertEqual(str(sq1), "[Square] (7) 7/7 - 7")

    def test_Square_update2(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq2 = Square(7, 7, 7, 7)
        sq2.update(1, 1)
        self.assertEqual(str(sq2), "[Square] (1) 7/7 - 1")

    def test_Square_update3(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq3 = Square(7, 7, 7, 7)
        MyList = [1, 2, 3]
        sq3.update(*MyList)
        self.assertEqual(str(sq3), "[Square] (1) 3/7 - 2")

    def test_Square_update4(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq4 = Square(7, 7, 7, 7)
        MyList = [1, 2, 3, 4]
        sq4.update(*MyList)
        self.assertEqual(str(sq4), "[Square] (1) 3/4 - 2")

    def test_Square_update5(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq5 = Square(7, 7, 7, 7)
        MyList = []
        sq5.update(*MyList)
        self.assertEqual(str(sq5), "[Square] (7) 7/7 - 7")

    def test_Square_update6(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq6 = Square(7, 7, 7, 7)
        MyDict = {'size': 1}
        sq6.update(**MyDict)
        self.assertEqual(str(sq6), "[Square] (7) 7/7 - 1")

    def test_Square_update7(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq7 = Square(7, 7, 7, 7)
        MyDict = {'id': 1, 'size': 1, 'x': 1, 'y': 1}
        sq7.update(**MyDict)
        self.assertEqual(str(sq7), "[Square] (1) 1/1 - 1")

    def test_Square_update8(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        sq7 = Square(7, 7, 7, 7)
        sq7.update()
        self.assertEqual(str(sq7), "[Square] (7) 7/7 - 7")

    def test_Square_update9(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            sq8 = Square(2)
            sq8.update(1, -2)

    def test_Square_update10(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq9 = Square(2)
            sq9.update(1, 2.7)

    def test_Square_update11(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq10 = Square(2)
            sq10.update(1, float('NaN'))

    def test_Square_update12(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq11 = Square(2)
            sq11.update(1, float('inf'))

    def test_Square_update13(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq12 = Square(2)
            sq12.update(1, 1e100)

    def test_Square_update14(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq12 = Square(2)
            sq12.update(1, 5j)

    def test_Square_update15(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            sq13 = Square(7, 7, 7, 7)
            sq13.update(1, True)

    def test_Square_update16(self):
        """Square testing update function"""
        Base._Base__nb_objects = 0
        with self.assertRaises(IndexError):
            sq14 = Square(7, 7, 7, 7)
            sq14.update(1, 2, 3, 4, 5)

    # SQUARE KWARGS
    def test1_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        r1 = Square(10, 10, 10, 10)
        r1.update(size=1)
        self.assertEqual(str(r1), "[Square] (10) 10/10 - 1")

    def test2_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        r2 = Square(10, 10, 10, 10)
        r2.update(size=3)
        self.assertEqual(str(r2), "[Square] (10) 10/10 - 3")

    def test3_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Square(10, 10, 10, 10)
            r3.update(size=0)

    def test4_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r4 = Square(10, 10, 10, 10)
            r4.update(x=-1)

    def test5_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r5 = Square(10, 10, 10, 10)
            r5.update(size=4.2)

    def test6_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r6 = Square(10, 10, 10, 10)
            r6.update(x=None)

    def test7_update_kwargs(self):
        """Square test updating kwargs"""
        Base._Base__nb_objects = 0
        r2 = Square(10, 10, 10, 10)
        r2.update(x=1, sizet=4)
        self.assertEqual(str(r2), "[Square] (10) 1/10 - 10")

    # CREATE
    def test_create1(self):
        """test normal use of create"""
        s1 = {'id': 89}
        s1c = Square.create(**s1)

    def test_create2(self):
        """test normal use of create"""
        s1 = {'id': 89, 'size': 1, 'x': 2, 'y': 3}
        s1c = Square.create(**s1)

    def test_create3(self):
        """test normal use of create"""
        s1 = {'id': 89, 'size': 1}
        s1c = Square.create(**s1)

if __name__ == '__main__':
    unittest.main()
