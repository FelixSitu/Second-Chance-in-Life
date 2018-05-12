import unittest
from char import *

class TestChar(unittest.TestCase):
   def test_lower(self):
      lower1 = is_lower_101("B")
      lower2 = is_lower_101("b")
      self.assertFalse(lower1)
      self.assertTrue(lower2)

   def test_char_rot(self):
       rot1 = char_rot_13("a")
       rot2 = char_rot_13('b')
       rot3 = char_rot_13('N')
       self.assertEqual(rot1,'n')
       self.assertEqual(rot2,'o')
       self.assertEqual(rot3,'A')

if __name__ == '__main__':
   unittest.main()

