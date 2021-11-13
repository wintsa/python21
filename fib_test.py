import unittest, fib


class MyTestCase(unittest.TestCase):
    def test_something(self):
        fib.fib(1)
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
