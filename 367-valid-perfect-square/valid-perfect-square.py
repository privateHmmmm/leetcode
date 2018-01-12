# -*- coding:utf-8 -*-


# Given a positive integer num, write a function which returns True if num is a perfect square else False.
#
#
# Note: Do not use any built-in library function such as sqrt.
#
#
# Example 1:
#
# Input: 16
# Returns: True
#
#
#
# Example 2:
#
# Input: 14
# Returns: False
#
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        lo, hi = 0, num
        
        while lo <= hi:
            # print lo, hi
            mid = (hi+lo)/2
            tmp = mid**2
            if tmp>num:
                hi = mid - 1
            elif tmp<num:
                lo = mid + 1
            else:
                return True
        
        return False
