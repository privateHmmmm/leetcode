# -*- coding:utf-8 -*-


# Given an integer array nums, find the sum of the elements between indices i and j (i &le; j), inclusive.
#
# Example:
#
# Given nums = [-2, 0, 3, -5, 2, -1]
#
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
#
#
#
# Note:
#
# You may assume that the array does not change.
# There are many calls to sumRange function.
#
#


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        
        self.nums = [0 for i in range(0, len(nums)+1)]
        for i in range(1, len(nums)+1):
            self.nums[i] = self.nums[i-1] + nums[i-1]

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        
        return self.nums[j+1] - self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
