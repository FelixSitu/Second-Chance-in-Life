import unittest
from map import *
from point import *

class TestCases(unittest.TestCase):
   def test_square_all(self):
       lst1 = [5,10]
       lst2 = [10,15]
       sqLst1 = square_all(lst1)
       sqlst2 = square_all(lst2)
       self.assertListEqual(sqLst1,[25, 100])
       self.assertListEqual(sqlst2,[100, 225])

   def test_add_n(self):
       lst1 = [5,10]
       lst2 = [10,15]
       addLst1 = add_n_all(lst1, 5)
       addLst2 = add_n_all(lst2, 10)
       self.assertListEqual(addLst1,[10,15])
       self.assertListEqual(addLst2,[20,25])

   def test_distance_all(self):
       lst1 = [Point(3,4)]
       lst2 = [Point(6,8)]
       disLst1 = distance_all(lst1)
       disLst2 = distance_all(lst2)
       self.assertListEqual(disLst1,[5.0])
       self.assertAlmostEqual(disLst2,[10.0])


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

