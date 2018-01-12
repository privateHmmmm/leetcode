# -*- coding:utf-8 -*-


#
# Given a collection of distinct numbers, return all possible permutations.
#
#
#
# For example,
# [1,2,3] have the following permutations:
#
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]
#
#


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List
        
        """
        
        """
        import collections
        def backtrack(nums, array, temp_dict):
            
            #print 'enter backtrack, temp_dict: %s, array: %s' %(temp_dict, array)
            if len(nums) == len(temp_dict.keys()):
                array.append(copy.copy(temp_dict.values()))
                return
            
            for i in range(0, len(nums)):
                if i in temp_dict:
                    continue
                temp_dict[i] = nums[i]
                backtrack(nums, array, temp_dict)
                temp_dict.pop(i)
            return
             
        nums.sort()
        array = []
        temp_dict = collections.OrderedDict()
        backtrack(nums, array, temp_dict)
        return array
        """
        
        res = []
        path = [0 for i in range(0, len(nums))]
        visited = [False for i in range(0, len(nums))]
        
        def robot(idx):
            
            if idx >= len(nums):
                res.append(copy.copy(path))
                return
            
            for i in range(0, len(nums)):
                if visited[i] == False:
                    visited[i] = True
                    path[idx] = nums[i]
                    robot(idx+1)
                    visited[i] = False
                    
        robot(0)
        return res
