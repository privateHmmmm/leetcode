# -*- coding:utf-8 -*-


# Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
#
#
#     For example, given array S = {-1 2 1 -4}, and target = 1.
#
#     The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
#


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        res = 2**31-1
        nums.sort()
        for i in range(0, len(nums)):
            if i > 0 and nums[i-1] == nums[i]: continue
            start, end = i+1, len(nums)-1
            while start<end:
                _sum = nums[i] + nums[start] + nums[end]
                if abs(target - _sum) < abs(target - res):
                    res = _sum
                if _sum == target: 
                    return res
                elif _sum > target:
                    end -= 1
                else:
                    start += 1
        
        return res
                        
