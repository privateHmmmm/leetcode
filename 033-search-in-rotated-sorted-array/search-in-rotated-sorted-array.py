# -*- coding:utf-8 -*-


# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        # time: O(n)
        if not nums: return -1
        L, R = 0, len(nums)-1
        
        while L + 1 < R:
            mid = (L+R)/2
            if nums[L] < nums[mid]:
                # increasing ..
                if nums[L] <= target <= nums[mid]:
                    R = mid
                else:
                    L = mid
            else: # nums[L] > nums[mid]
                if nums[mid] <= target <= nums[R]:
                    L = mid
                else:
                    R = mid
        
        if target == nums[R]: 
            return R
        elif target == nums[L]:
            return L
        else:
            return -1
                
