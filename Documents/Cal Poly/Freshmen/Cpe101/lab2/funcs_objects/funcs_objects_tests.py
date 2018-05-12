import unittest
from objects import *

from funcs_object import *
import math

class TestCases(unittest.TestCase):
   def test_point(self):
       center1 = Point(1.0, 2.0)
       center2 = Point(4.0, 6.0)
       self.assertAlmostEqual(center1.x,1.0)
       self.assertAlmostEqual(center1.y,2.0)
       self.assertAlmostEqual(center2.x,4.0)
       self.assertAlmostEqual(center2.y,6.0)


   def test_circle(self):
       center1 = Point(1.0, 2.0)
       center2 = Point(4.0, 6.0)
       radius = 3
       circle1 = Circle(center1,radius)
       circle2 = Circle(center2,radius)
       self.assertAlmostEqual(circle1.radius,3)
       self.assertAlmostEqual(circle2.radius,3)

   def test_distance(self):
       self.assertAlmostEqual(distance(Point(1,2),Point(3,4)),2.8284271247461903)

   def test_circles_overlap(self):
       cir1 = Circle(Point(1,2),3)
       cir2 = Circle(Point(3,4),3)
       overlap = circle_overlap(cir1,cir2)
       self.assertTrue(overlap)


   # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

