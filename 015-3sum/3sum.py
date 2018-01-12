# -*- coding:utf-8 -*-


# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note: The solution set must not contain duplicate triplets.
#
#
# For example, given array S = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) < 3: return []
        
        res = []
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] > 0: continue # !!!!
            if i != 0 and nums[i-1] == nums[i]: continue
            start, end = i+1, len(nums)-1
            while start< end:
                _sum = nums[start] + nums[end] + nums[i]
                if _sum == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
                    while start<=end and nums[start-1] == nums[start]: start += 1
                    while end>=start and nums[end+1] == nums[end]: end -= 1
                elif _sum > 0:
                    end -= 1
                else:
                    start += 1
        
        return res
            
