#!/usr/bin/python3
"""Unittest for Base class"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os


class TestBase(unittest.TestCase):
    """Test cases for the Base class"""

    def setUp(self):
        """Reset __nb_objects before each test"""
        Base._Base__nb_objects = 0

    def test_id_assignment(self):
        """Test id assignment"""
        b1 = Base()
        self.assertEqual(b1.id, 1)

        b2 = Base()
        self.assertEqual(b2.id, 2)

        b3 = Base(12)
        self.assertEqual(b3.id, 12)

        b4 = Base()
        self.assertEqual(b4.id, 3)

    def test_to_json_string(self):
        """Test to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertTrue(isinstance(json_dictionary, str))
        self.assertEqual(json_dictionary, '[{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}]')

    def test_save_to_file(self):
        """Test save_to_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", "r") as file:
            self.assertTrue(len(file.read()) > 0)
        os.remove("Rectangle.json")

    def test_from_json_string(self):
        """Test from_json_string method"""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4}, 
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertTrue(isinstance(list_output, list))
        self.assertEqual(list_output, list_input)

    def test_create(self):
        """Test create method"""
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)
        self.assertEqual(str(r1), str(r2))

    def test_load_from_file(self):
        """Test load_from_file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in list_rectangles_output))
        self.assertEqual(len(list_rectangles_output), 2)
        os.remove("Rectangle.json")

    def test_save_to_file_csv(self):
        """Test save_to_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        with open("Rectangle.csv", "r") as file:
            self.assertTrue(len(file.read()) > 0)
        os.remove("Rectangle.csv")

    def test_load_from_file_csv(self):
        """Test load_from_file_csv method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertTrue(all(isinstance(obj, Rectangle) for obj in list_rectangles_output))
        self.assertEqual(len(list_rectangles_output), 2)
        os.remove("Rectangle.csv")


if __name__ == '__main__':
    unittest.main()