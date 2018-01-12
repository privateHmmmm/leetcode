# -*- coding:utf-8 -*-


#
# Follow up for "Search in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
#
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Write a function to determine if a given target is in the array.
#
# The array may contain duplicates.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        # time: O(n)
        if not nums: return False
        L, R = 0, len(nums)-1
        
        while L < R:
            mid = (R-L)/2+L
            if nums[mid] == target: return True
            if nums[mid] < nums[R]:
                if nums[mid] <= target and nums[R] >= target:
                    L = mid + 1
                else:
                    R = mid - 1
            elif nums[mid] > nums[R]:
                if nums[L] <= target and nums[mid] >= target:
                    R = mid - 1
                else:
                    L = mid + 1
            else:
                R -= 1
        
        return nums[L] == target
                
