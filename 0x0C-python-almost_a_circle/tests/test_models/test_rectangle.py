#!/usr/bin/python3
"""Unittest for Rectangle class
"""
import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestingRectangle(unittest.TestCase):
    """class for Test Rectangle"""

    # RECTANGLE WIDTH
    def test0_width_few_args(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r0 = Rectangle(1)

    def test1_width_string(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r1 = Rectangle("hello", 2)

    def test2_width_list(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r2 = Rectangle([9, 6], 2)

    def test3_width_tuple(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r3 = Rectangle((7, 3), 4)

    def test4_width_dictionary(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r4 = Rectangle({'k': 8}, 5)

    def test5_width_zero(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(ValueError):
                r5 = Rectangle(0, 6)

    def test6_width_negative(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(ValueError):
                r6 = Rectangle(-7, 8)

    def test7_width_float(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r7 = Rectangle(4.5, 9)

    def test8_width_nan(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r8 = Rectangle(float('NaN'), 7)

    def test9_width_inf(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r9 = Rectangle(float('inf'), 7)

    def test10_width_boolean(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r10 = Rectangle(True, 1)

    def test11_width_many_args(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r11 = Rectangle(1, 2, 3, 4, 5, 6)

    def test12_width_no_args(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r12 = Rectangle()

    def test13_width_impossible(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r13 = Rectangle(5j, 8)

    def test14_width_big_num(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r14 = Rectangle(1e100, 7)

    def test15_width_none(self):
            """Width Rectangle"""
            Base._Base__nb_objects = 0
            with self.assertRaises(TypeError):
                r15 = Rectangle(None)

    # RECTANGLE HEIGHT
    def test0_height_string(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "hello")

    def test1_height_list(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, [9, 6])

    def test2_height_tuple(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, (7, 3))

    def test3_height_dictionary(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r4 = Rectangle(5, {'k': 8})

    def test4_height_zero(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r5 = Rectangle(6, 0)

    def test5_height_negative(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r6 = Rectangle(8, -7)

    def test6_height_float(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r7 = Rectangle(9, 4.5)

    def test7_height_nan(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r8 = Rectangle(7, float('NaN'))

    def test8_height_inf(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r9 = Rectangle(7, float('inf'))

    def test9_height_boolean(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r10 = Rectangle(1, True)

    def test10_height_more_args(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r11 = Rectangle(1, 2, 3, 4, 5, 6)

    def test11_height_no_args(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r12 = Rectangle()

    def test12_height_impossible(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r13 = Rectangle(8, 5j)

    def test13_height_big_num(self):
        """Rectangle Height"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r14 = Rectangle(7, 1e100)

    # RECTANGLE X
    def test0_x_string(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, "hello")

    def test1_x_list(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r2 = Rectangle(2, 2, [9, 6])

    def test2_x_tuple(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(3, 4, (7, 3))

    def test3_x_dictionary(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r4 = Rectangle(4, 5, {'k': 8})

    def test4_x_negative(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 8, -7)

    def test5_x_float(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 9, 4.5)

    def test6_x_nan(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 7, float('NaN'))

    def test7_x_inf(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 7, float('inf'))

    def test8_x_boolean(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 1, True)

    def test9_x_more_args(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

    def test10_no_args(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r12 = Rectangle()

    def test11_x_impossible(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r13 = Rectangle(12, 8, 5j)

    def test12_x_big_num(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r14 = Rectangle(13, 7, 1e100)

    def test13_x_zero(self):
        """Rectangle X """
        Base._Base__nb_objects = 0
        rect = Rectangle(9, 8, 0)
        self.assertEqual(rect.x, 0)

    # RECTANGLE Y
    def test0_y_string(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 1, 2, "hello")

    def test1_y_list(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r2 = Rectangle(3, 2, 2, [9, 6])

    def test2_y_tuple(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r3 = Rectangle(4, 3, 4, (7, 3))

    def test3_y_dictionary(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r4 = Rectangle(5, 4, 5, {'k': 8})

    def test4_y_negative(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r6 = Rectangle(6, 6, 8, -7)

    def test5_y_float(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r7 = Rectangle(7, 7, 9, 4.5)

    def test6_y_nan(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r8 = Rectangle(8, 8, 7, float('NaN'))

    def test7_y_inf(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r9 = Rectangle(9, 9, 7, float('inf'))

    def test8_y_boolean(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r10 = Rectangle(10, 10, 1, True)

    def test9_y_more_args(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r11 = Rectangle(11, 1, 2, 3, 4, 5, 6)

    def test10_y_empty(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r12 = Rectangle()

    def test11_y_impossible(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r13 = Rectangle(11, 12, 8, 5j)

    def test12_y_big_num(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r14 = Rectangle(12, 13, 7, 1e100)

    def test13_y_zero(self):
        """Rectangle Y"""
        Base._Base__nb_objects = 0
        rect = Rectangle(9, 8, 6, 0)
        self.assertEqual(rect.y, 0)

    # RECTANGLE AREA
    def test1_areaRect(self):
        """Rectangle test area"""
        Base._Base__nb_objects = 0
        rect = Rectangle(4, 4)
        self.assertEqual(rect.area(), 16)

    # RECTANGLE REASSIGN
    def test0_reassign_x(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        rect = Rectangle(1, 2, 3, 4, 5)
        rect.x = 1
        self.assertEqual(rect.x, 1)

    def test1_reassign_width(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.width = 3
        self.assertEqual(rect1.width, 3)

    def test2_reassign_negative(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect2 = Rectangle(1, 2, 3, 4, 5)
            rect2.width = -1

    def test3_reassign_string(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect3 = Rectangle(1, 2, 3, 4, 5)
            rect3.width = "hello"

    def test4_reassign_list(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect4 = Rectangle(1, 2, 3, 4, 5)
            rect4.width = [9, 6]

    def test5_reassign_tuple(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect5 = Rectangle(1, 2, 3, 4, 5)
            rect5.y = (7, 3)

    def test6_reassign_dictionary(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect6 = Rectangle(1, 2, 3, 4, 5)
            rect6.height = {'k': 8}

    def test7_reassign_zero_height(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect7 = Rectangle(1, 2, 3, 4, 5)
            rect7.height = 0

    def test8_reassign_zero_x(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(1, 2, 3, 4, 5)
        rect1.x = 0
        self.assertEqual(rect1.x, 0)

    def test9_reassign_float(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect8 = Rectangle(1, 2, 3, 4, 5)
            rect8.height = 4.5

    def test10_reassign_nan(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect8 = Rectangle(1, 2, 3, 4, 5)
            rect8.height = float('NaN')

    def test11_reassign_inf(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect9 = Rectangle(1, 2, 3, 4, 5)
            rect9.height = float('inf')

    def test12_reassign_boolean(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect9 = Rectangle(1, 2, 3, 4, 5)
            rect9.x = True

    def test13_reassign_impossible(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect10 = Rectangle(1, 2, 3, 4, 5)
            rect10.x = 5j

    def test14_reassign_big(self):
        """Test reasign values Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect11 = Rectangle(1, 2, 3, 4, 5)
            rect11.y = 1e100

    # UPDATE RECTANGLE
    def test0_assign(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect1 = Rectangle(7, 7, 7, 7, 7)
        self.assertEqual(str(rect1), "[Rectangle] (7) 7/7 - 7/7")

    def test1_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect2 = Rectangle(7, 7, 7, 7, 7)
        rect2.update(1, 1)
        self.assertEqual(str(rect2), "[Rectangle] (1) 7/7 - 1/7")

    def test2_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect3 = Rectangle(7, 7, 7, 7, 7)
        MyList = [1, 2, 3]
        rect3.update(*MyList)
        self.assertEqual(str(rect3), "[Rectangle] (1) 7/7 - 2/3")

    def test3_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect4 = Rectangle(7, 7, 7, 7, 7)
        MyList = [1, 2, 3, 4]
        rect4.update(*MyList)
        self.assertEqual(str(rect4), "[Rectangle] (1) 4/7 - 2/3")

    def test4_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect5 = Rectangle(7, 7, 7, 7, 7)
        MyList = []
        rect5.update(*MyList)
        self.assertEqual(str(rect5), "[Rectangle] (7) 7/7 - 7/7")

    def test5_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect6 = Rectangle(7, 7, 7, 7, 7)
        MyDict = {'width': 1, 'height': 1}
        rect6.update(**MyDict)
        self.assertEqual(str(rect6), "[Rectangle] (7) 7/7 - 1/1")

    def test6_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect7 = Rectangle(7, 7, 7, 7, 7)
        MyDict = {'id': 1, 'width': 1, 'height': 1, 'x': 1, 'y': 1}
        rect7.update(**MyDict)
        self.assertEqual(str(rect7), "[Rectangle] (1) 1/1 - 1/1")

    def test7_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        rect7 = Rectangle(7, 7, 7, 7, 7)
        rect7.update()
        self.assertEqual(str(rect7), "[Rectangle] (7) 7/7 - 7/7")

    def test8_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            rect8 = Rectangle(2, 2)
            rect8.update(1, -2)

    def test9_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect9 = Rectangle(2, 2)
            rect9.update(1, 2.7)

    def test10_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect10 = Rectangle(2, 2)
            rect10.update(1, float('NaN'))

    def test11_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect11 = Rectangle(2, 2)
            rect11.update(1, float('inf'))

    def test12_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect12 = Rectangle(2, 2)
            rect12.update(1, 1e100)

    def test13_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect12 = Rectangle(2, 2)
            rect12.update(1, 5j)

    def test14_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect6 = Rectangle(7, 7, 7, 7, 7)
            rect6.update(1, True)

    def test15_update(self):
        """Update Rectangle"""
        Base._Base__nb_objects = 0
        with self.assertRaises(IndexError):
            rect7 = Rectangle(7, 7, 7, 7, 7)
            rect7.update(1, 2, 3, 4, 5, 6)

    # RECTANGLE STR
    def test_stRect_1(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect1 = Rectangle()
            rect1 = str(self)

    def test_stRect_2(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect2 = Rectangle()
            rect2 = str(self)

    def test_stRect_3(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        rect3 = Rectangle(1, 2)
        self.assertEqual(str(rect3), "[Rectangle] (1) 0/0 - 1/2")

    def test_stRect_4(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        rect4 = Rectangle(1, 2, 3)
        self.assertEqual(str(rect4), "[Rectangle] (1) 3/0 - 1/2")

    def test_stRect_5(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        rect5 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(str(rect5), "[Rectangle] (5) 3/4 - 1/2")

    def test_stRect_6(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect6 = Rectangle(1, 2, 3, 4, 5, 6)
            rect6 = str(self)

    def test_stRect_7(self):
        """Rectangle test str"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect7 = Rectangle(None)
            rect7 = str(self)

    # RECTANGLE TO_DICTIONARY
    def test1_todict(self):
        """Rectangle test to_dictionary """
        Base._Base__nb_objects = 0
        rect = Rectangle(1, 2, 3, 4, 5)
        rect1 = rect.to_dictionary()
        MyDict = {'id': 5, 'width': 1, 'height': 2, 'x': 3, 'y': 4}
        for i in MyDict:
            self.assertEqual(rect1[i], MyDict[i])

    def test2_todict(self):
        """Rectangle test to_dictionary """
        Base._Base__nb_objects = 0
        rect = Rectangle(1, 2)
        rect1 = rect.to_dictionary()
        MyDict = {'id': 1, 'width': 1, 'height': 2, 'x': 0, 'y': 0}
        for i in MyDict:
            self.assertEqual(rect1[i], MyDict[i])

    def test3_todict(self):
        """Rectangle test to_dictionary """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect = Rectangle()
            rect1 = rect.to_dictionary()

    def test4_todict(self):
        """Rectangle test to_dictionary """
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            rect = Rectangle(None)
            rect1 = rect.to_dictionary()

    # RECTANGLE KWARGS
    def test1_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1)
        self.assertEqual(str(r1), "[Rectangle] (1) 10/10 - 10/1")

    def test2_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(width=3)
        self.assertEqual(str(r2), "[Rectangle] (1) 10/10 - 3/10")

    def test3_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r3 = Rectangle(10, 10, 10, 10)
            r3.update(width=0)

    def test4_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        with self.assertRaises(ValueError):
            r4 = Rectangle(10, 10, 10, 10)
            r4.update(x=-1)

    def test5_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r5 = Rectangle(10, 10, 10, 10)
            r5.update(width=4.2)

    def test6_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        with self.assertRaises(TypeError):
            r6 = Rectangle(10, 10, 10, 10)
            r6.update(x=None)

    def test7_update_kwargs(self):
        """RECTANGLE KWARGS"""
        Base._Base__nb_objects = 0
        r2 = Rectangle(10, 10, 10, 10)
        r2.update(x=1, height=4, width=3)
        self.assertEqual(str(r2), "[Rectangle] (1) 1/10 - 3/4")

if __name__ == '__main__':
    unittest.main()
