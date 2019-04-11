
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:    
       raise ValueError()     #raises ValueError if list is None
   
   if not int_list:
       return None            #returns None if list is empty
   
   max = int_list[0]          #sets initial max to be the first value in the list
   for x in int_list:         #for loop goes through each value, makes it the new max if greater than current max
       if x > max:
           max = x
   return max

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
       raise ValueError()     #raises ValueError if list is None
   
   if len(int_list) == 0:
       return []              #returns an empty list if the list is empty

   #the statement below returns a list of the final value in int_list plus the reversed version of the rest of int_list
   return [int_list[len(int_list) - 1]] + reverse_rec(int_list[:len(int_list) - 1])

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
       raise ValueError()     #raises ValueError if list is None
     
   if low > high:
       return None            #base case: if low is greater than high, the list can not be split in half anymore

   mid = int((low + high) / 2)#sets mid as the index halfway between low and high
   if int_list[mid] == target:
       return mid             #returns mid if the value at mid in the list is the target

   if int_list[mid] > target: 
       return bin_search(target, low, mid-1, int_list)#searches for the target in the lower half of the list
   elif int_list[mid] < target:
       return bin_search(target, mid+1, high, int_list)#searches for the target in the upper half of the list
