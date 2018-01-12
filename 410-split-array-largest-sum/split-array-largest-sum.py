# -*- coding:utf-8 -*-


# Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.
#
#
# Note:
# If n is the length of array, assume the following constraints are satisfied:
#
# 1 &le; n &le; 1000
# 1 &le; m &le; min(50, n)
#
#
#
# Examples: 
#
# Input:
# nums = [7,2,5,10,8]
# m = 2
#
# Output:
# 18
#
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#
#


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        
        def guess(nums, g, m):
            
            Sum = 0
            for num in nums:
                if Sum + num > g:
                    m = m - 1
                    if num > g:
                        return False
                    Sum = num
                else:
                    Sum += num
            
            return m >= 1
        
        L = 0
        R = sum(nums)
        ans = 0
        
        while L<=R:
            mid = (L+R)/2
            if (guess(nums, mid, m)):
                ans = mid
                # L = mid + 1
                R = mid - 1
            else:
                L = mid + 1
                # R = mid - 1
        
        return ans
