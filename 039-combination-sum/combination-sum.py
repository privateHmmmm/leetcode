# -*- coding:utf-8 -*-


#
# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T. 
#
#
# The same repeated number may be chosen from C unlimited number of times.
#
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
#
# [
#   [7],
#   [2, 2, 3]
# ]
#
#


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        path = []
        candidates.sort()
        
        def helper(start, _sum):
            
            if _sum == target:
                res.append(copy.copy(path))
                return
            elif _sum > target:
                return
            
            for i in range(start, len(candidates)):
                if target - _sum < candidates[i]: break
                path.append(candidates[i])
                helper(i, _sum+candidates[i])
                path.pop()
        
        helper(0, 0)
        return res
        
        
        
    
        """
        res = []
        path = []
            
        candidates.sort()
            
        def dfs(idx, _sum):
            
            if _sum == target:
                res.append(copy.copy(path))
                return
            
            if idx>=len(candidates) or _sum>target:
                return
            
            if _sum + candidates[idx] <= target:
                path.append(candidates[idx])    
                dfs(idx, _sum + candidates[idx])
                path.pop()
                
            dfs(idx+1, _sum)
        
        dfs(0, 0)
        return res
        """
    
#         res = []
#         path = []
            
#         candidates.sort()
        
#         def dfs(idx, _sum):
#             if _sum == target:
#                 res.append(copy.copy(path))
#                 return
            
#             if idx>=len(candidates) or _sum+candidates[idx]>target:
#                 return
            
#             for i in range(idx, len(candidates)):
#                 path.append(candidates[i])
#                 dfs(i, _sum+candidates[i])
#                 path.pop()
        
#         dfs(0, 0)
#         return res
            
