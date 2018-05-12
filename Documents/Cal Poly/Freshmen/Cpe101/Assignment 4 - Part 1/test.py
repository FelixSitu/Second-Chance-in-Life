import unittest
from vector_math import *
from cast import *


class Test_cases(unittest.TestCase):
   def test_cast_all_ray(self):
       center1 = Point(-2, 0, 0)
       sphere1 = Sphere(center1, 1)
       center2 = Point(-4, -2, 0)
       sphere2 = Sphere(center2, 2)
       center3 = Point(5, 4, 3)
       sphere3 = Sphere(center3, 3)
       sphereLst = [sphere1,sphere2,sphere3]
       castRay1 = cast_ray(Ray(Point(-14,0,0),Vector(1,0,0)),sphereLst)
       self.assertTrue(castRay1)


if __name__ == '__main__':
    unittest.main()
