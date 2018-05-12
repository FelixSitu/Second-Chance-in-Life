import unittest
from conditional import *


class TestCases(unittest.TestCase):
    def test_case(self):
        max1 = max_101(4,2)
        max2 = max_101(100,1000)
        self.assertAlmostEqual(max1, 4)
        self.assertAlmostEqual(max2, 1000)

    def test_max_of_three(self):
        max1 = max_of_three(100, 200, 300)
        max2 = max_of_three(10000, 2000, 30)
        max3 = max_of_three(100, 3000, 310)
        self.assertAlmostEqual(max1, 300)
        self.assertAlmostEqual(max2, 10000)
        self.assertAlmostEqual(max3, 3000)

    def rental_late_free(self):
        x0 = rental_late_fee(0)
        x1 = rental_late_fee(5)
        x2 = rental_late_fee(10)
        x3 = rental_late_fee(20)
        x4 = rental_late_fee(30)
        self.assertAlmostEqual(x0, 0)
        self.assertAlmostEqual(x1, 5)
        self.assertAlmostEqual(x2, 7)
        self.assertAlmostEqual(x3, 19)
        self.assertAlmostEqual(x4, 100)

# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

