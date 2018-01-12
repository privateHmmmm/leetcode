# -*- coding:utf-8 -*-


# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = 0; R = len(nums)-1
        while L < R:
            mid = (L+R)/2
            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid
        
        return nums[L]
            
