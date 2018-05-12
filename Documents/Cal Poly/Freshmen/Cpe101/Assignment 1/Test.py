from Data import *
import unittest

class Test_cases(unittest.TestCase):
   def test_point(self):
      myPoint1 = Point(1,1,1)
      myPoint2 = Point(2,2,2)
      self.assertAlmostEqual(myPoint1.x,1)
      self.assertAlmostEqual(myPoint1.y,1)
      self.assertAlmostEqual(myPoint1.z,1)
      self.assertAlmostEqual(myPoint2.x, 2)
      self.assertAlmostEqual(myPoint2.y, 2)
      self.assertAlmostEqual(myPoint2.z, 2)

   def test_vector(self):
       vec1 = Vector(3,3,3)
       vec2 = Vector(4,4,4)
       self.assertAlmostEqual(vec1.xdir,3)
       self.assertAlmostEqual(vec1.ydir,3)
       self.assertAlmostEqual(vec1.zdir,3)
       self.assertAlmostEqual(vec2.xdir, 4)
       self.assertAlmostEqual(vec2.ydir, 4)
       self.assertAlmostEqual(vec2.zdir, 4)

   def test_ray(self):
       myPoint1 = Point(1,1,1)
       myPoint2 = Point(2,2,2)
       vec1 = Vector(3,3,3)
       vec2 = Vector(4,4,4)
       ray1 = Ray(myPoint1,vec1)
       ray2 = Ray(myPoint2,vec2)
       self.assertAlmostEqual(ray1.pt.x,1)
       self.assertAlmostEqual(ray1.pt.y,1)
       self.assertAlmostEqual(ray1.pt.z,1)
       self.assertAlmostEqual(ray1.dir.xdir,3)
       self.assertAlmostEqual(ray1.dir.ydir, 3)
       self.assertAlmostEqual(ray1.dir.zdir, 3)
       self.assertAlmostEqual(ray2.pt.x, 2)
       self.assertAlmostEqual(ray2.pt.y, 2)
       self.assertAlmostEqual(ray2.pt.z, 2)
       self.assertAlmostEqual(ray2.dir.xdir, 4)
       self.assertAlmostEqual(ray2.dir.ydir, 4)
       self.assertAlmostEqual(ray2.dir.zdir, 4)

   def test_sphere(self):
       cen1 = Point(1,1,1)
       cen2 = Point(2,2,2)
       rad1 = 3
       rad2 = 4
       ball1 = Sphere(cen1,rad1)
       ball2 = Sphere(cen2,rad2)
       self.assertAlmostEqual(ball1.center.x,1)
       self.assertAlmostEqual(ball1.center.y, 1)
       self.assertAlmostEqual(ball1.center.z, 1)
       self.assertAlmostEqual(ball1.radius,3)
       self.assertAlmostEqual(ball2.center.x, 2)
       self.assertAlmostEqual(ball2.center.y, 2)
       self.assertAlmostEqual(ball2.center.z, 2)
       self.assertAlmostEqual(ball2.radius, 4)


if __name__ == '__main__':
   unittest.main()