import imp
import unittest
from exercises import twenty_three

class TestTwentyTwo(unittest.TestCase):
    def test_string_is_upper(self):
        self.assertTrue(twenty_three.is_string_upper("TEST"))
    
    def test_string_is_not_upper(self):
        self.assertFalse(twenty_three.is_string_upper("Test"))
    
    def test_error_isRaised(self):
        self.assertIsNone(twenty_three.is_string_upper(1))

if __name__ == "__main__":
    unittest.main()
