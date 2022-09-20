import unittest
from exercises import twenty

class TestTwenty(unittest.TestCase):
    def test_is_prime_number(self):
        self.assertTrue(twenty.is_num_prime(5))
        self.assertTrue(twenty.is_num_prime(53))
        self.assertTrue(twenty.is_num_prime(89))

    def test_is_not_prime_number(self):
        self.assertFalse(twenty.is_num_prime(51))
        self.assertFalse(twenty.is_num_prime(58))
        self.assertFalse(twenty.is_num_prime(87))

if __name__ == "__main__":
    unittest.main()