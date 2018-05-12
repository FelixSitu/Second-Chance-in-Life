import unittest
from collisions import *
from Data import *

class Test_cases(unittest.TestCase):


   def test_practice(self):
      quad1 = quadratic_formula(4,5,1)
      #print quad1
      self.assertListEqual(quad1,[-0.25, -1.0])

   def test_sphere_intersection_point(self):
       point1 = Point(0,0,0)
       vec1 = Vector(1,0,0)
       ray1 = Ray(point1,vec1)
       center1 = Point(0,0,0)
       sphere1 = Sphere(center1,5)
       computeCo = compute_coefficient(sphere1,ray1)
       #print computeCo
       #self.assertAlmostEqual(computeCo,(1,-10,24))
       interSphere = sphere_intersection_point(ray1,sphere1)
       #print interSphere
       self.assertEqual(interSphere, Point(x=5.0,y=0.0,z=0.0))

   def test_find_intersection_points(self):
       point1 = Point(0, 0, 0)
       vec1 = Vector(0, 0, 1)
       ray1 = Ray(point1, vec1)
       center1 = Point(0,0,8)
       sphere1 = Sphere(center1,1)
       center2 = Point(0,0,10)
       sphere2 = Sphere(center2,2)
       center3 = Point(0,0,-3)
       sphere3 = Sphere(center3,1)
       sphereLst = [sphere1,sphere2,sphere3]
       points = find_intersection_points(sphereLst, ray1)
       #print points
       self.assertListEqual(points,[(sphere1,Point(0.,0.,7.)),(sphere2,Point(0.0,0.0,8.0))])

   def test_sphere_at_point(self):
       center1 = Point(-2,0,0)
       sphere1 = Sphere(center1,1)
       point1 = Point(5,4,3)
       sphereNorm = sphere_normal_at_point(sphere1,point1)
       print sphereNorm
       self.assertAlmostEqual(sphereNorm,Vector(-0.813733471207,-0.464990554975,-0.348742916231))

if __name__ == '__main__':
   unittest.main()
