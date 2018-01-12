# -*- coding:utf-8 -*-


# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Also thanks to @ts for adding additional test cases.


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        result = {}
        def robot(idx):
            
            if idx<0:
                return 0
            
            if idx in result: return result[idx]
            result[idx] = max(robot(idx-1), nums[idx]+robot(idx-2))
            return result[idx]
        
        if not nums:
            return 0
        return robot(len(nums)-1)
        """
        
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        DP = [0 for i in range(0, len(nums))]
        DP[0] = nums[0]
        DP[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            DP[i] = max(DP[i-1], nums[i]+DP[i-2])
        
        return DP[-1]
        
        
