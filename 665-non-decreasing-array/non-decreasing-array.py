# -*- coding:utf-8 -*-


#
# Given an array with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
#
#
#
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
#
#
# Example 1:
#
# Input: [4,2,3]
# Output: True
# Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
#
#
#
# Example 2:
#
# Input: [4,2,1]
# Output: False
# Explanation: You can't get a non-decreasing array by modify at most one element.
#
#
#
# Note:
# The n belongs to [1, 10,000].
#


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        index=-1
        for i in range(0, len(nums)):
            if i >0 and nums[i] < nums[i-1]:
                if index == -1:
                    index=i
                else:
                    return False
        
        print index
        
        if index == -1:
            return True
        else:
            # index must >= 1
            if (index == len(nums)-1 or nums[index-1] <= nums[index+1]) \
                or (index == 1 or nums[index-2] <= nums[index]):
                return True
            else:
                return False
                     
