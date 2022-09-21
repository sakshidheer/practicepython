import unittest
from exercises import five

class Exercise5Test(unittest.TestCase):
    def test_num_is_prime(self):
        num = 13
        self.assertTrue(five.is_prime_number(num))

    def test_num_is_not_prime(self):
        num = 6
        self.assertFalse(five.is_prime_number(num)) 

if __name__ == '__main__':
    unittest.main()