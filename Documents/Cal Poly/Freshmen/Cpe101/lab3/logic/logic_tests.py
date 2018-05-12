import unittest
from logic import *


class TestCases(unittest.TestCase):
    def test_case(self):
        x1 = is_even(10)
        x2 = is_even(9)
        self.assertTrue(x1)
        self.assertFalse(x2)
        self.assertTrue(is_even(18))

    def test_interval(self):
        # x1 is (10,20]
        x1 = is_an_interval(15, 10, 20)
        # x2 is (12,23]
        x2 = is_an_interval(5, 12, 23)
        self.assertTrue(x1)
        self.assertFalse(x2)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

