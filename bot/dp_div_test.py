import unittest
from dp_div import numberWays, minWays

class DpDivTest(unittest.TestCase):
    def test_4_is_5(self):
        self.assertEqual(numberWays(4), 5)
    def test_7_is_10(self):
        self.assertEqual(numberWays(7), 10)
    def test_min_ways_7_is_3(self):
        self.assertEqual(minWays(7), 3)


if __name__ == '__main__':
    unittest.main()
