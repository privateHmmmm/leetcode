# -*- coding:utf-8 -*-


#
# Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.
#
#
# Example 1:
#
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
#
#
#
# Note:
#
# 1 <= k <= n <= 30,000.
# Elements of the given array will be in the range [-10,000, 10,000].
#
#


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        # if len(nums) == k:
            # return float(sum(nums))/k
        
        Sum = 0 
        Max = -10001*k
        for i, num in enumerate(nums):
            if i < k:
                Sum += num
            else:
                Max = max(Max, Sum)
                Sum += (nums[i] - nums[i-k])
        
        Max = max(Max, Sum)
        return float(Max)/k
                
        
