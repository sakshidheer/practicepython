import unittest
from exercises import sixteen

class TestSixteen(unittest.TestCase):
    def test_piramid_for_7(self):
        with self.assertLogs() as captured:
            sixteen.log_piramid(7)
        self.assertEqual(len(captured.records), 7)
        self.assertEqual(captured.records[0].getMessage(), "      *") 
        self.assertEqual(captured.records[1].getMessage(), "     ***") 
        self.assertEqual(captured.records[2].getMessage(), "    *****") 
        self.assertEqual(captured.records[3].getMessage(), "   *******") 
        self.assertEqual(captured.records[4].getMessage(), "  *********") 
        self.assertEqual(captured.records[5].getMessage(), " ***********") 
        self.assertEqual(captured.records[6].getMessage(), "*************") 