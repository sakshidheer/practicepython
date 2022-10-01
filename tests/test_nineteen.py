import unittest
from exercises import nineteen

class TestNineteen(unittest.TestCase):
    def test_get_square_root(self):
        self.assertEqual(nineteen.get_square_root(4),2)

    def test_get_square_roor_for_negative_number(self):
        with self.assertRaises(ValueError):
            nineteen.get_square_root(-3)