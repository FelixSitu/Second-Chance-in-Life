import unittest
from groups import *

class TestGroups(unittest.TestCase):

   def assertListAlmostEqual(self, l1, l2):
      self.assertEqual(len(l1), len(l2))
      for el1, el2 in zip(l1, l2):
         self.assertAlmostEqual(el1, el2)

   def test_group3(self):
      lst1 = [1,2,3,4,5,6,7,8,9]
      lst2 = [1,2,3,4,5,6,7,8]
      groupLst1 = groups_of_3(lst1)
      groupLst2 = groups_of_3(lst2)
      self.assertListEqual(groupLst1,[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
      self.assertListEqual(groupLst2,[[1, 2, 3], [4, 5, 6], [7, 8]])

if __name__ == '__main__':
   unittest.main()
