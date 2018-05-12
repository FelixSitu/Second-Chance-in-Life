import unittest
from string_101 import *

class TestString(unittest.TestCase):
   def test_rot_13(self):
      oldstring1 = "a"
      oldstring2 = "b"
      oldstring3 = "A"
      newstring1 = str_rot_13(oldstring1)
      newstring2 = str_rot_13(oldstring2)
      newstring3 = str_rot_13(oldstring3)
      self.assertEqual(newstring1,"T")
      self.assertEqual(newstring2,"U")
      self.assertEqual(newstring3,"N")

   def test_str_trans(self):
      word1 = "abcabc"
      trans1 = str_translate_101(word1,"a","x")
      self.assertEqual(trans1,"xbcxbc")

if __name__ == '__main__':
   unittest.main()

