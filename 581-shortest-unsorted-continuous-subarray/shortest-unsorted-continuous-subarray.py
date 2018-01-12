# -*- coding:utf-8 -*-


# Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.  
#
# You need to find the shortest such subarray and output its length.
#
# Example 1:
#
# Input: [2, 6, 4, 8, 10, 9, 15]
# Output: 5
# Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
#
#
#
# Note:
#
# Then length of the input array is in range [1, 10,000].
# The input array may contain duplicates, so ascending order here means <=. 
#
#


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        start = -1
        end = -1
        for i in range(0, len(nums)-1):
            if nums[i] > min(nums[i+1:]):
                start = i
                break
        
        if start == -1:
            return 0
        
        for j in range(len(nums)-1, 0, -1):
            if nums[j] < max(nums[:j]):
                end = j
                break
      
        return end-start+1
        """
        
        n = len(nums)
        end = -2
        start = -1
        Max = nums[0] 
        Min = nums[n-1]
        
        for i in range(0, n):
            Max = max(Max, nums[i])
            if nums[i] < Max:
                end = i
            
            Min = min(Min, nums[n-1-i])
            if nums[n-1-i] > Min:
                start = n-1-i
        
        return end-start+1
                
