# -*- coding:utf-8 -*-


#
# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
#
# Your algorithm should run in O(n) complexity.
#


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = 0
        _set = set(nums)
        
        for i in range(0, len(nums)):
            down = nums[i]-1
            while down in _set:
                _set.remove(down)
                down -=1
            up = nums[i] + 1
            while up in _set:
                _set.remove(up)
                up += 1
            res = max(res, up - down - 1)
        
        return res
            
