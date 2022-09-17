import imp
import unittest
from exercises import TwentyTwo

class TestTwentyTwo(unittest.TestCase):
    def test_string_is_upper(self):
        self.assertTrue(TwentyTwo.is_string_upper("TEST"))
    
    def test_string_is_not_upper(self):
        self.assertFalse(TwentyTwo.is_string_upper("Test"))
    
    def test_error_isRaised(self):
        self.assertIsNone(TwentyTwo.is_string_upper(1))

if __name__ == "__main__":
    unittest.main()
