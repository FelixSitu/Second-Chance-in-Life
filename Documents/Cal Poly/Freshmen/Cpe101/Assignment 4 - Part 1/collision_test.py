import unittest
from collisions import *
from Data import *

class Test_cases(unittest.TestCase):
   def test_sphere_intersection_point(self):
       point1 = Point(0,0,0)
       vec1 = Vector(1,0,0)
       ray1 = Ray(point1,vec1)
       center1 = Point(0,0,0)
       sphere1 = Sphere(center1,1)
       computeCo = compute_coefficient(sphere1,ray1)
       #print computeCo
       #self.assertAlmostEqual(computeCo,(1,-10,24))
       interSphere = sphere_intersection_point(ray1,sphere1)
       print interSphere
       #self.assertEqual(interSphere, Point(x=4.0,y=0.0,z=0.0))

if __name__ == '__main__':
   unittest.main()
