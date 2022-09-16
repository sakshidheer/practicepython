import unittest
from exercises import Five

class Exercise5Test(unittest.TestCase):
    def test_num_is_prime(self):
        num = 13
        self.assertTrue(Five.is_prime_number(num))

    def test_num_is_not_prime(self):
        num = 6
        self.assertFalse(Five.is_prime_number(num)) 

if __name__ == '__main__':
    unittest.main()