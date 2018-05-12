import unittest
from vector_math import *

class TestCases(unittest.TestCase):
    def test_scale_vector(self):
        vec1 = Vector(1.0,2.0,3.0)
        vector1 = scale_vector(vec1,1.5)
        self.assertAlmostEqual(vector1,Vector(1.5,3.0,4.5))

    def test_dot_vector(self):
        vec1 = Vector(1.0,2.0,3.0)
        vec2 = Vector(4.0,5.0,6.0)
        dotVector = dot_vector(vec1,vec2)
        self.assertAlmostEqual(dotVector,32)

    def test_length_vector(self):
        vec1 = Vector(1,2,3)
        vector1 = length_vector(vec1)
        self.assertAlmostEqual(vector1, 3.7416573867739413)

    def test_normalized_vector(self):
        vec1 = Vector(1,2,3)
        vector1 = normalize_vector(vec1)
        self.assertAlmostEqual(vector1,Vector(0.2672612419124244, 0.5345224838248488, 0.8017837257372732))

    def test_difference_point(self):
        pt1 = Point(1,2,3)
        pt2 = Point(4,5,6)
        diffPoint = difference_point(pt1,pt2)
        self.assertAlmostEqual(diffPoint,3,3,3)

    def test_difference_vector(self):
        vec1 = Vector(1,2,3)
        vec2 = Vector(4,5,6)
        diffVector = difference_vector(vec1,vec2)
        self.assertAlmostEqual(diffVector,Vector(3,3,3))

    def test_trans_point(self):
        pt1 = Point(1,2,3)
        vec1 = Vector(4,5,6)
        transPoint = translate_point(pt1,vec1)
        self.assertAlmostEqual(transPoint,Vector(5,7,9))

    def test_vector_from_to(self):
        pt1 = Point(1,2,3)
        pt2 = Point(4,5,6)
        vector1 = vector_from_to(pt1,pt2)
        self.assertEquals(vector1,Vector(3,3,3))

if __name__ == '__main__':
    unittest.main()