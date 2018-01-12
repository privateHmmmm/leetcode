# -*- coding:utf-8 -*-


# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ans = 0
        while n:
            n = n/5
            ans += n
        
        return ans
