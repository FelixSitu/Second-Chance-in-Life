import unittest
from filter import *
import point

class TestCases(unittest.TestCase):
   def test_are_positive(self):
      lst1 = [1,5]
      lst2 = [1,-5]
      posLst1 = are_positive(lst1)
      posLst2 = are_positive(lst2)
      self.assertListEqual(posLst1,[1,5])
      self.assertListEqual(posLst2,[1])

   def test_are_greater_than(self):
       lst1 = [0,5]
       n1 = 3
       lst2 = [5,15]
       n2 = 12
       greatLst1 = are_greater_than(lst1,n1)
       greatLst2 = are_greater_than(lst2,n2)
       self.assertListEqual(greatLst1,[5])
       self.assertListEqual(greatLst2,[15])

   def test_in_first_quad(self):
       lst1 = [Point(3,4),Point(5,6),Point(-5,5)]
       lst2 = [Point(1,2),Point(-1,2),Point(0,0)]
       firstLst1 = are_in_first_quadrant(lst1)
       firstLst2 = are_in_first_quadrant(lst2)
       self.assertListEqual(firstLst1,[Point(3,4),Point(5,6)])
       self.assertListEqual(firstLst2,[Point(1,2)])

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

