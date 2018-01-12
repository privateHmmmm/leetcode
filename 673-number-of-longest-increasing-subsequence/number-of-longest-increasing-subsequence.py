# -*- coding:utf-8 -*-


#
# Given an unsorted array of integers, find the number of longest increasing subsequence.
#
#
# Example 1:
#
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1, 3, 5, 7].
#
#
#
# Example 2:
#
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
#
#
#
# Note:
# Length of the given array will be not exceed 2000 and the answer is guaranteed to be fit in 32-bit signed int.
#


class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return 0
        
        lens = [1 for i in range(0, len(nums))]
        counter = [1 for i in range(0, len(nums))]
        
        for i in range(0, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    if lens[i] < lens[j]+1:
                        lens[i] = lens[j]+1
                        counter[i] = counter[j]
                    elif lens[i] == lens[j]+1:
                        counter[i] +=counter[j]
                    
        # print lens, counter
        Max=max(lens)
        res = 0
        for i in range(0, len(nums)):
            if lens[i] == Max:
                res += counter[i]
        return res
    
