# -*- coding:utf-8 -*-


#
# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
#
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
#


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums: return 0
        
        _max = nums[0]
        _min = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            imax = max(_max*nums[i], _min*nums[i], nums[i])
            _min = min(_max*nums[i], _min*nums[i], nums[i])
            _max = imax
            res = max(res, _max)
        
        return res
