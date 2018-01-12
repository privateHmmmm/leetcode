# -*- coding:utf-8 -*-


#
# Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.
#
#
# If there are multiple solutions, return any subset is fine.
#
#
# Example 1:
#
# nums: [1,2,3]
#
# Result: [1,2] (of course, [1,3] will also be ok)
#
#
#
# Example 2:
#
# nums: [1,2,4,8]
#
# Result: [1,2,4,8]
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating all test cases.


class Solution(object):
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        
        if not nums:
            return []
        
        dp = [0 for i in range(0, len(nums))]
        parents = [0 for i in range(0, len(nums))]
        mx = 0
        mx_idx = 0
        
        nums.sort()
        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    parents[i] = j
                    if mx < dp[i]:
                        mx = dp[i]
                        mx_idx = i
            
        print dp, parents
    
        res = []
        for i in range(0, mx):
            res.append(nums[mx_idx])
            mx_idx = parents[mx_idx]
        return res
    
