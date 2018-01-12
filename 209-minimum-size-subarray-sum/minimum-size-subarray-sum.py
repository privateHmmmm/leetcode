# -*- coding:utf-8 -*-


#
# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum &ge; s. If there isn't one, return 0 instead.
#
#
# For example, given the array [2,3,1,2,4,3] and s = 7,
# the subarray [4,3] has the minimal length under the problem constraint.
#
#
# click to show more practice.
#
# More practice:
#
# If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
#
#
# Credits:Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        
        if sum(nums) < s:
            return 0
        
        i = 0
        j = 0
        lens=len(nums)
        mi = lens
        Sum =0 
        
        while Sum < s and j < lens:
            Sum +=nums[j]
            
            while Sum >= s:
                mi=min(mi, j-i+1)
                Sum -=nums[i]
                i +=1
            
            j +=1
        
        return mi
