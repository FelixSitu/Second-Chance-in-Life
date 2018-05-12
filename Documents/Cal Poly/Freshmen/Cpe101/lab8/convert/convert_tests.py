import unittest
from convert import *

class TestConvert(unittest.TestCase):
   def test_convert(self):
          string1 = "12345678xyz"
          string2 = "12345678"
          float1 = float_default(string1)
          float2 = float_default(string2)
          self.assertEquals(float1,"12345678xyz")
          self.assertEquals(float2, 12345678.0)

   def test_practice(self):
       print practice(6)


if __name__ == '__main__':
   unittest.main()

