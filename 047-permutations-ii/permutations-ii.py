# -*- coding:utf-8 -*-


#
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
#
#
# For example,
# [1,1,2] have the following unique permutations:
#
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
#
#


class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        res = []
        path = [0 for i in range(0, len(nums))]
        visited = [False for i in range(0, len(nums))]
        
        def robot(idx):
            
            if idx >= len(nums):
                res.append(copy.copy(path))
                return
            
            for i in range(0, len(nums)):
                if i !=0 and nums[i-1] == nums[i] and visited[i-1] == False:
                    continue
                
                if visited[i] == False:
                    visited[i] = True
                    path[idx] = nums[i]
                    robot(idx+1)
                    visited[i] = False
                    
        robot(0)
        return res
