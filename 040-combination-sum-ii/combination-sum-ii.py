# -*- coding:utf-8 -*-


#
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#
#
# Each number in C may only be used once in the combination.
#
# Note:
#
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
#
#
#
#
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
#
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
#
#


class Solution(object):
    def combinationSum2(self, candidates, target):
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
                if _sum + candidates[i] > target: break
                if i > start and candidates[i-1] == candidates[i]: continue
                path.append(candidates[i])
                helper(i+1, _sum+candidates[i])
                path.pop()
        
        helper(0, 0)
        return res

