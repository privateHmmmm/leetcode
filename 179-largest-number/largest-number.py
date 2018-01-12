# -*- coding:utf-8 -*-


# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        if not nums: return ""
        array = [str(num) for num in nums]
        array.sort(reverse=True, cmp=lambda a,b: -1 if a+b < b+a else 0)
        
        if array[0]  == '0':
            return '0'
        return ''.join(array)
