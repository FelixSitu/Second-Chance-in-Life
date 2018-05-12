import unittest
from point import *
import utility


class TestCases(unittest.TestCase):
    def test_point_one(self):
        pt = Point(1, 2)
        self.assertAlmostEqual(pt.x, 1)
        self.assertAlmostEqual(pt.y, 2)

    def test_point_two(self):
        pt = Point(-4.7, 19.2)
        self.assertAlmostEqual(pt.x, -4.7)
        self.assertAlmostEqual(pt.y, 19.2)

    def test_equality1(self):
        pt1 = Point(1.0, 1.0)
        pt2 = Point(1.0, 1.0)
        self.assertEqual(pt1, pt2)

    def test_equality2(self):
        pt1 = Point(2.0, 2.0)
        pt2 = Point(2.0, 2.0)
        self.assertEqual(pt1, pt2)

    def test_equality3(self):
        pt1 = Point(1.0, 2.0)
        pt2 = Point(-4.7, 19.2)
        self.assertNotEqual(pt1, pt2)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()

