import unittest
from models.square import Square

class TestSquare(unittest.TestCase):
    
    def test_initialization(self):
        """Test initializing a square with size and default attributes."""
        sq = Square(5)
        self.assertEqual(sq.size, 5)
        self.assertEqual(sq.x, 0)
        self.assertEqual(sq.y, 0)
        self.assertIsNotNone(sq.id)

    def test_custom_initialization(self):
        """Test initializing a square with custom values."""
        sq = Square(3, 2, 1, 42)
        self.assertEqual(sq.size, 3)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 1)
        self.assertEqual(sq.id, 42)

    def test_size_setter_and_getter(self):
        """Test the size property."""
        sq = Square(4)
        sq.size = 10
        self.assertEqual(sq.size, 10)
        self.assertEqual(sq.width, 10)
        self.assertEqual(sq.height, 10)

    def test_invalid_size(self):
        """Test size setter with invalid values."""
        sq = Square(5)
        with self.assertRaises(TypeError):
            sq.size = "not an int"
        with self.assertRaises(ValueError):
            sq.size = -10

    def test_update_with_args(self):
        """Test updating square attributes using *args."""
        sq = Square(2, 0, 0, 10)
        sq.update(99, 7, 3, 4)
        self.assertEqual(sq.id, 99)
        self.assertEqual(sq.size, 7)
        self.assertEqual(sq.x, 3)
        self.assertEqual(sq.y, 4)

    def test_update_with_kwargs(self):
        """Test updating square attributes using **kwargs."""
        sq = Square(4)
        sq.update(id=42, size=8, x=2, y=1)
        self.assertEqual(sq.id, 42)
        self.assertEqual(sq.size, 8)
        self.assertEqual(sq.x, 2)
        self.assertEqual(sq.y, 1)

    def test_area(self):
        """Test the area method."""
        sq = Square(6)
        self.assertEqual(sq.area(), 36)

    def test_display(self):
        """Test the display method output."""
        sq = Square(2, 1, 1)
        expected_output = "\n ##\n ##\n"
        from io import StringIO
        import sys
        captured_output = StringIO()
        sys.stdout = captured_output
        sq.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_to_dictionary(self):
        """Test the to_dictionary method."""
        sq = Square(5, 1, 2, 99)
        expected_dict = {'id': 99, 'size': 5, 'x': 1, 'y': 2}
        self.assertDictEqual(sq.to_dictionary(), expected_dict)

if __name__ == "__main__":
    unittest.main()
