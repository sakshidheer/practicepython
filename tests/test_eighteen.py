import unittest
from exercises import eighteen

class TestEighteen(unittest.TestCase):
    def test_alphabet_is_constant(self):
        self.assertEqual(eighteen.get_alphabet_type('y'),'Constant')
        self.assertEqual(eighteen.get_alphabet_type('f'),'Constant')
    
    def test_alphabet_is_vowel(self):
        self.assertEqual(eighteen.get_alphabet_type('a'),'Vowel')
        self.assertEqual(eighteen.get_alphabet_type('o'),'Vowel')

if __name__ == "__main__":
    unittest.main()