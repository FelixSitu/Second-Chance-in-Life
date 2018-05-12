import unittest
from poly import *

class TestPoly(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_addpoly(self):
      poly1 = [2.3,4.7,1.0]
      poly2 = [1.2,2.1,-3.2]
      poly3 = poly_add2(poly1,poly2)
      self.assertListAlmostEqual(poly3,[3.5, 6.8, -2.2])

   def test_multpoly(self):
      lst1 = [1,2,3]
      lst2 = [4,5,6]
      lst3 = [2,3.1,2.7]
      poly1 = poly_mult2(lst1,lst2)
      poly2 = poly_mult2(lst3,lst3)
      self.assertAlmostEqual(poly1,[9, 27, 28, 13, 5])
      self.assertAlmostEqual(poly2,[5.4, 16.740000000000002, 20.410000000000004, 12.4, 4])

if __name__ == '__main__':
   unittest.main()
