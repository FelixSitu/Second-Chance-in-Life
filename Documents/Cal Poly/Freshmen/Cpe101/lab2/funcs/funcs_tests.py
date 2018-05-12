import unittest
from funcs import *
import math

class TestCases(unittest.TestCase):
   def test_f(self):
       self.assertAlmostEqual(f(10),720)
       self.assertAlmostEqual(f(20), 2840)

   def test_g(self):
      self.assertAlmostEqual(g(1,2), 5)
      self.assertAlmostEqual(g(5,10), 125)

   def test_hypotenuse(self):
       self.assertAlmostEqual(h(3,4), 5)
       self.assertAlmostEqual(h(6,8), 10)

   def test_is_positive(self):
       self.assertTrue(is_positive(1),True)
       self.assertFalse(is_positive(-1),False)


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

