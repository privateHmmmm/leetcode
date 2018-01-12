# -*- coding:utf-8 -*-


#
# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # 1 1 1 3 1
        
        L, R=0, len(nums)-1
        while L<=R:
            mid = (R-L)/2+L
            if nums[mid] < nums[R]:
                R = mid
            elif nums[mid] > nums[R]:
                L = mid + 1
            else:
                R -=1
        
        return nums[L]
        
