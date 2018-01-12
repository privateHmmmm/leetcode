# -*- coding:utf-8 -*-


# Implement pow(x, n).
#
#
#
#
# Example 1:
#
# Input: 2.00000, 10
# Output: 1024.00000
#
#
#
# Example 2:
#
# Input: 2.10000, 3
# Output: 9.26100
#
#


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0: return 1
        
        if n < 0:
            x = 1/x
            n = -n
        
        t = self.myPow(x, n/2)
        if n % 2 == 0:
            return t*t
        else:
            return t*t*x
        
