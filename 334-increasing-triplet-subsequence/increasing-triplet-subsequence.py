# -*- coding:utf-8 -*-


#
# Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.
#
#
# Formally the function should:
# Return true if there exists i, j, k  
# such that arr[i] &lt; arr[j] &lt; arr[k] given 0 &le; i &lt; j &lt; k &le; n-1 
# else return false.
#
#
#
# Your algorithm should run in O(n) time complexity and O(1) space complexity.
#
#
# Examples:
# Given [1, 2, 3, 4, 5],
# return true.
#
#
# Given [5, 4, 3, 2, 1],
# return false.
#
#
# Credits:Special thanks to @DjangoUnchained for adding this problem and creating all test cases.


class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        min1 = 2**31 - 1
        min2 = 2**31 - 1
        
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            elif num > min2:
                return True
            
        return False
