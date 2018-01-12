# -*- coding:utf-8 -*-


# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
#
#
# Note:
#
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
#
#
#
# Example 1:
#
# Input: [1, 5, 11, 5]
#
# Output: true
#
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#
#
#
# Example 2:
#
# Input: [1, 2, 3, 5]
#
# Output: false
#
# Explanation: The array cannot be partitioned into equal sum subsets.
#
#


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        def backtrace(lists, cur, target):
        
            if cur == target:
                return True
        
            for i in range(0, len(lists)):
                if lists[i] + cur > target:
                    continue    
                if True == backtrace(lists[i+1:], lists[i]+cur, target):
                    return True
                
            return False
            
        
        Sum = sum(nums)
        if Sum % 2 == 1:
            return False
        
        target = Sum/2
        cur = 0
        return backtrace(nums, cur, target)
        """
        
        Sum = sum(nums)
        if Sum % 2 == 1:
            return False
        
        target = Sum/2
        if max(nums) > target:
            return False
        
        DP = [[False for j in range(0, target+1)] for i in range(0, len(nums))]
        # sum j can be gotten from the first (i+1) nums
        
        # if nums[0] <= target:
        DP[0][nums[0]] = True
        
        for i in range(1, len(nums)):
            for j in range(0, target+1):
                DP[i][j] = DP[i-1][j]
                if j>=nums[i]:
                    DP[i][j] |= DP[i-1][j - nums[i]]
        
        return DP[len(nums)-1][target]
        
