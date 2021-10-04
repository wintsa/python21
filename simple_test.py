import simple
import unittest

class SimpleTest(unittest.TestCase):
    def test_simple_add_3_and_2_is_5(self):
        self.assertEqual(simple.add(3, 2), 5)

if __name__=='__main__':
    unittest.main()