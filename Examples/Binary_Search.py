# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 07:36:45 2019

@author: hp
"""

# Returns index of x in arr if present, else -1 
def binarySearch (arr, l, r, x): 
    """
    Find the indices of arr in arr.

    Args:
        arr: (array): write your description
        l: (int): write your description
        r: (int): write your description
        x: (int): write your description
    """
  
    # Check base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarySearch(arr, mid+1, r, x) 
  
    else: 
        # Element is not present in the array 
        return -1
