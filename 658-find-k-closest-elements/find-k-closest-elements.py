# -*- coding:utf-8 -*-


#
# Given a sorted array, two integers k and x, find the k closest elements to x in the array.  The result should also be sorted in ascending order.
# If there is a tie,  the smaller elements are always preferred.
#
#
# Example 1:
#
# Input: [1,2,3,4,5], k=4, x=3
# Output: [1,2,3,4]
#
#
#
#
# Example 2:
#
# Input: [1,2,3,4,5], k=4, x=-1
# Output: [1,2,3,4]
#
#
#
# Note:
#
# The value k is positive and will always be smaller than the length of the sorted array.
#  Length of the given array is positive and will not exceed 104
#  Absolute value of elements in the array and x will not exceed 104
#
#
#
#
#
#
# UPDATE (2017/9/19):
# The arr parameter had been changed to an array of integers (instead of a list of integers). Please reload the code definition to get the latest changes.
#


class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        
        res = []
        for i, num in enumerate(arr):
            if num >= x:
                if not res: res = arr[max(0, i - k):i]
                if len(res) < k:
                    res.append(num)
                elif abs(res[0]-x) > abs(num-x):
                    res.pop(0)
                    res.append(num)
                else:
                    break
        if not res: res = arr[-k:]
        return res
                    
        # binary search is better ...
                
                
        
