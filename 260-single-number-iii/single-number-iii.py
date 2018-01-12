# -*- coding:utf-8 -*-


#
# Given an array of numbers nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once.
#
#
# For example:
#
#
# Given nums = [1, 2, 1, 3, 2, 5], return [3, 5].
#
#
# Note:
#
# The order of the result is not important. So in the above example, [5, 3] is also correct.
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant space complexity?
#
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        # time: O(n), space: O(1)
        
        diff = 0
        for num in nums:
            diff ^= num
        
        diff &= (-diff)
        
        res = [0] * 2
        for num in nums:
            if num & diff == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        
        return res
