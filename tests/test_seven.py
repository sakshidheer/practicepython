import imp
import unittest
from exercises import seven

class TestSeven(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(seven.get_factorial(7),5040)
        self.assertEqual(seven.get_factorial(19),121645100408832000)

if __name__ == "__main__":
    unittest.main()