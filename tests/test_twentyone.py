import unittest
from exercises import TwentyOne

class TestTwentyTwo(unittest.TestCase):
    def test_order_is_one(self):
        self.assertEqual(TwentyOne.get_order(1),1)
    
    def test_order_is_Four(self):
        self.assertEqual(TwentyOne.get_order(1890),4)

    def test_order_is_Ten(self):
        self.assertEqual(TwentyOne.get_order(1890333333),10)

if __name__ == "__main__":
    unittest.main()