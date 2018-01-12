# -*- coding:utf-8 -*-


# Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
#
# For example,
# Given [5, 7, 7, 8, 8, 10] and target value 8,
# return [3, 4].
#


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if not nums: return [-1, -1]
        res = [-1, -1]
        # find left bound
        L, R = 0, len(nums)-1
        while L+1 < R:
            mid = (L+R)/2
            if nums[mid] >= target:
                R = mid
            else: # numd[mid] < target
                L = mid + 1
                
        if nums[L] == target: 
            res[0] = L
        elif nums[R] == target:
            res[0] = R
        else:
            return res
        
        # find right bound
        L, R = 0, len(nums)-1
        while L+1 < R:
            mid = (L+R)/2
            if nums[mid] <= target:
                L = mid 
            else: # numd[mid] > target
                R = mid - 1
                
        if nums[R] == target: 
            res[1] = R
        else:
            res[1] = L
        
        return res
        
        
        
        
        
        
        
        
#         ans = [-1, -1]
        
#         # left bound
#         L, R = 0, len(nums)-1
#         while L<=R:
#             mid = (L+R)/2
#             if nums[mid] < target:
#                 L = mid + 1
#             else:
#                 R = mid - 1 
#                 if nums[mid] == target:
#                     ans[0] = mid      
                        
#         # right bound
#         L, R = 0, len(nums)-1
#         while L<=R:
#             mid = (L+R)/2
#             if nums[mid] <= target:
#                 L = mid + 1
#                 if nums[mid] == target:
#                     ans[1] = mid
#             else:
#                 R = mid - 1 
        
#         return ans
