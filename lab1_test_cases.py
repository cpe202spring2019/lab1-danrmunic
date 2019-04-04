import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)
        
        tlist = []
        self.assertEqual(max_list_iter(tlist), None)

        tlist = [5,6,3,8,19,-4,0]
        self.assertEqual(max_list_iter(tlist), 19)


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([5,6,3,8,19,-4,0]), [0,-4,19,8,3,6,5])
        self.assertEqual(reverse_rec([]), [])


    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0,0,0,tlist)

        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        self.assertEqual(bin_search(5, 0, 6, [5,6,3,8,19,-4,0]), 0)
        #self.assertEqual(bin_search(3, 0, 0, [1,2,3], None)
        #self.assertEqual(bin_search(3, 0, 3, [1,2,4], None)

if __name__ == "__main__":
        unittest.main()

    
