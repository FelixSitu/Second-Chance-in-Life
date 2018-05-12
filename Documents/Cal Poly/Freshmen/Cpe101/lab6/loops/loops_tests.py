import unittest
from loops import *

class TestLoops(unittest.TestCase):
   def test_for(self):
      self.assertEqual(for_version([1,2,3]), [3,2,1])

   def test_while(self):
      self.assertEqual(while_version([1,2,3]), [3,2,1])

if __name__ == '__main__':
   unittest.main()

