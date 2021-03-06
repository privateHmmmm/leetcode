# -*- coding:utf-8 -*-


#
# Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
#
#
# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.
#
#
# click to show more practice.
#
# More practice:
#
# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
#


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        Max=nums[0]
        Sum=0
        #pre_sum=0
        for i in range(0, len(nums)):
            if nums[i] > 0:
                if Sum < 0:
                    Sum = 0
                    #positive_sum=0
            Sum += nums[i]
            if Sum > Max:
                Max=Sum
            else:
                if Max < nums[i]:
                    Max = nums[i]
            #    positive_sum +=nums[i]
                
        return Max
