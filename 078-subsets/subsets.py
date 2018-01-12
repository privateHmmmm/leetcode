# -*- coding:utf-8 -*-


#
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
#
# For example,
# If nums = [1,2,3], a solution is:
#
#
#
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        
        def dfs(idx, ans, n, use):
            
            if idx >= n: # bound and record
                tmp = []
                for i in range(0, len(use)):
                    if use[i] == True:
                        tmp.append(nums[i])
                ans.append(tmp)
                return
            
            # only have to look at it's children
            use[idx] = True
            dfs(idx+1, ans, n, use)
            use[idx] = False
            dfs(idx+1, ans, n, use)
        
        ans = []
        use = [False for i in range(len(nums))]
        dfs(0, ans, len(nums), use)
        return ans
    
