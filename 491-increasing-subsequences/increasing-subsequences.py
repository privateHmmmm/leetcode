# -*- coding:utf-8 -*-


#
# Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2 .
#
#
# Example:
#
# Input: [4, 6, 7, 7]
# Output: [[4, 6], [4, 7], [4, 6, 7], [4, 6, 7, 7], [6, 7], [6, 7, 7], [7,7], [4,7,7]]
#
#
#
# Note:
#
# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.
#
#


class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        cur=[]
        res=[]
        
        def dfs(index):
            
            if len(cur)>=2:
                res.append(copy.copy(cur))
            
            Sets=set()
            for i in range(index, len(nums)):
                if (not cur or nums[i] >= cur[-1]) and nums[i] not in Sets:
                    cur.append(nums[i])
                    Sets.add(nums[i])
                    dfs(i+1)
                    cur.pop()
            
        dfs(0)
        return res
        
