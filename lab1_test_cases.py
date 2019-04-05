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
        self.assertIsNone(max_list_iter(tlist)) #test return None for an empty list

        tlist = [5,6,3,8,19,-4,0]
        self.assertEqual(max_list_iter(tlist), 19) #test for functionality

        tlist = [1,2]
        self.assertEqual(max_list_iter(tlist), 2)
        tlist = [2,1]
        self.assertEqual(max_list_iter(tlist), 2)  #test for endpoints


    def test_reverse_rec(self):
        tlist = None
        with self.assertRaises(ValueError):
            reverse_rec(tlist)

        self.assertEqual(reverse_rec([1,2,3]),[3,2,1]) #test for functionality
        self.assertEqual(reverse_rec([5,6,3,8,19,-4,0]), [0,-4,19,8,3,6,5]) #test unsorted list 
        self.assertEqual(reverse_rec([]), []) #test for empty list


    def test_bin_search(self):
        tlist = None
        with self.assertRaises(ValueError):
            bin_search(0,0,0,tlist)

        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 ) #test for functionality
        self.assertEqual(bin_search(-4, 0, 6, [-4, 0, 3, 5, 6, 8, 19]), 0) #tests if it can find first endpoint
        self.assertIsNone(bin_search(3, 0, 0, [1,2,3])) #tests if a number will not be found if it is not in the range
        self.assertIsNone(bin_search(3, 0, 3, [1,2,4])) #tests if a number will not be found if it is not in the list
        self.assertEqual(bin_search(19, 0, 6, [-4, 0, 3, 5, 6, 8, 19]), 6) #tests if it can find last endpoint

if __name__ == "__main__":
        unittest.main()

    
