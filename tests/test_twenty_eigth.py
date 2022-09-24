import unittest
from exercises import twenty_eigth

class TestTwentyEigth(unittest.TestCase):
    def test_get_age(self):
        student = twenty_eigth.Student(1, "Amit",2, 5, 1996)
        self.assertEqual(student.get_age(),26)\

if __name__ == "__main__":
    unittest.main()