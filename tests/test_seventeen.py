import unittest
from exercises import seventeen

class TestEighteen(unittest.TestCase):
    def test_lists_is_invese_mirror(self):
        list1 = [2,3,4,5,6]
        list2 = [6,5,4,3,2]
        self.assertTrue(seventeen.is_list_mirror_inverse(list1, list2))
        
    
    def test_lists_is_not_invese_mirror(self):
        list1 = [2,3,4,5,6]
        list2 = [6,5,4,3,1]
        self.assertFalse(seventeen.is_list_mirror_inverse(list1, list2))
    
    def test_lists_is_not_invese_mirror_when_length_is_not_equal(self):
        list1 = [2,3,4,5,6]
        list2 = [6,5,4,3]
        self.assertFalse(seventeen.is_list_mirror_inverse(list1, list2))

if __name__ == "__main__":
    unittest.main()