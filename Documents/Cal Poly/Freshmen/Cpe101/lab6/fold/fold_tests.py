import unittest
from fold import *
from point import *

class TestCases(unittest.TestCase):
   def test_1(self):
      lst1 = [0,1,2,3,4]
      lst2 = [-2,-1,0,1,2]
      sumLst1 = sum(lst1)
      sumLst2 = sum(lst2)
      self.assertAlmostEqual(sumLst1,10)
      self.assertAlmostEqual(sumLst2,0)
      sum2Lst1 = sum2(lst1)
      sum2Lst2 = sum2(lst2)
      self.assertAlmostEqual(sum2Lst1,10)
      self.assertAlmostEqual(sum2Lst2,0)

   def test_2(self):
      lst1 = [0,1,2,3,4,-2,-4,-6]
      lst2 = []
      smallLst1 = index_of_smallest(lst1)
      smallLst2 = index_of_smallest(lst2)
      self.assertAlmostEqual(smallLst1,7)
      self.assertAlmostEqual(smallLst2, None)

   """def test_3(self):
       lst1 = [Point(180,200),Point(2000,4000),Point(60,80)]
       originLst1 = nearest_origin(lst1)
       self.assertAlmostEqual(originLst1,2)
       lst2 = [Point(20, 40), Point(3, 4), Point(100, 80)]
       originLst2 = nearest_origin(lst2)
       self.assertAlmostEqual(originLst2, 1)"""

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

