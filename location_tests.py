import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_repr2(self):
        loc = Location("1rr4  0", 90, -180)
        self.assertEqual(repr(loc),"Location('1rr4  0', 90, -180)")
    
    def test_repr3(self):
        loc = Location("", 0, 0)
        self.assertEqual(repr(loc),"Location('', 0, 0)")

   
   # Add more tests!

if __name__ == "__main__":
        unittest.main()
