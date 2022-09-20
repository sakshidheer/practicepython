import unittest
from exercises import TwentyOne

class TestTwentyTwo(unittest.TestCase):
    def test_order_is_one(self):
        self.assertEqual(TwentyOne.get_order(1),1)
    
    def test_order_is_Four(self):
        self.assertEqual(TwentyOne.get_order(1890),4)

    def test_order_is_Ten(self):
        self.assertEqual(TwentyOne.get_order(1890333333),10)
    
    def test_number_is_armstrong(self):
        self.assertTrue(TwentyOne.is_num_armstrong(153))
        self.assertTrue(TwentyOne.is_num_armstrong(9))
        self.assertTrue(TwentyOne.is_num_armstrong(1634))
        self.assertTrue(TwentyOne.is_num_armstrong(9800817))
    
    def test_number_is_not_armstrong(self):
        self.assertFalse(TwentyOne.is_num_armstrong(152))
        self.assertFalse(TwentyOne.is_num_armstrong(19))
        self.assertFalse(TwentyOne.is_num_armstrong(1635))
        self.assertFalse(TwentyOne.is_num_armstrong(9800816))

if __name__ == "__main__":
    unittest.main()