import unittest
from vector_math import *
from cast import *
from Data import *


class Test_cases(unittest.TestCase):
   def test_cast_ray(self):
       red = Color(255, 0, 0)
       blue = Color(0, 0, 255)
       sphere1 = Sphere(Point(0.5, 1.5, -3.0), 2.5,red)
       sphere2 = Sphere(Point(1.0, 1.0, 0.0), 2,blue)
       sphereLst = [sphere1,sphere2]
       ray = Ray(Point(0, 0, -14), Vector(0, 0, 1))
       cast1 = cast_ray(ray,sphereLst)
       print cast1
       #self.assertListEqual(cast1,[[sphere1,Point(0.5, 1.5, -3.0),2.5,Color(255,0,0)]])

   """def test_cast_all_ray(self):
       eyepoint = Point(0.0, 0.0, -14.0)
       red = Color(255, 0, 0)
       blue = Color(0, 0, 255)
       sphere1 = Sphere(Point(0.5, 1.5, -3.0), 0.5, red)
       sphere2 = Sphere(Point(1.0, 1.0, 0.0), 2, blue)
       sphereLst = [sphere1,sphere2]
       ray = Ray(Point(0, 0, -14), Vector(0, 0, 1))
       cast1 = cast_all_rays(-10, 10, -7.5, 7.5, 512, 384, eyepoint, sphereLst)
       #print cast1"""

   """def test_cast_ray(self):
       point1 = Point(0, 0, 0)
       vec1 = Vector(0, 0, 1)
       ray1 = Ray(point1, vec1)
       center1 = Point(0, 0, 8)
       sphere1 = Sphere(center1, 1)
       center2 = Point(0, 0, 10)
       sphere2 = Sphere(center2, 2)
       center3 = Point(0, 0, -3)
       sphere3 = Sphere(center3, 1)
       sphereLst = [sphere1, sphere2]
       points = find_intersection_points(sphereLst,ray1)
       points1 = cast_ray(ray1,sphereLst)
       #print points
       self.assertListEqual(points1, [[sphere1, Point(0., 0., 7.)], [sphere2, Point(0.0, 0.0, 8.0)]])
       self.assertListEqual(points, [[sphere1, Point(0., 0., 7.)], [sphere2, Point(0.0, 0.0, 8.0)]])"""

if __name__ == '__main__':
    unittest.main()
