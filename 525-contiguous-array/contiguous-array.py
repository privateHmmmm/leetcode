# -*- coding:utf-8 -*-


# Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 
#
#
# Example 1:
#
# Input: [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
#
#
#
# Example 2:
#
# Input: [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
#
#
#
# Note:
# The length of the given binary array will not exceed 50,000.
#


class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dicts = {0: -1}
        
        # dicts[0].append(-1)
        diff = 0 # nums of 0 - nums of 1
        Max = 0
        for i in range(0, len(nums)):
            diff += (1 if nums[i] == 0 else -1)
            # dicts[diff].append(i)
            if diff in dicts:
                Max = max(Max, i-dicts[diff])
            else:
                dicts[diff] = i
        return Max
        # print dicts
        # Max = 0
        # for diff in dicts.keys():
            # Max = max(Max, dicts[diff][-1] - dicts[diff][0])
        
        # return Max
            
        
        
