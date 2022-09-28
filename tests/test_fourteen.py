import unittest
from exercises import fourteen

class Exercise5Test(unittest.TestCase):
    def test_num_is_prime(self):
        num = 13
        self.assertEquals(fourteen.calculate_simple_interest(10000,5,5),2500)


if __name__ == '__main__':
    unittest.main()