import unittest
from exercises import twentyseven

class TestTwentySeven(unittest.TestCase):
    def test_fizz_buzzwith_10(self):
        list_to_be_expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz']
        self.assertListEqual(twentyseven.generate_fizz_buzz_series(10),list_to_be_expected)
    
    def test_fizz_buzzwith_10(self):
        list_to_be_expected = [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 
'Fizz', 16, 17, 'Fizz', 19, 'Buzz']
        self.assertListEqual(twentyseven.generate_fizz_buzz_series(20),list_to_be_expected)

if __name__ == "__main__":
    unittest.main()