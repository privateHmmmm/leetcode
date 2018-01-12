# -*- coding:utf-8 -*-


# Implement int sqrt(int x).
#
# Compute and return the square root of x.
#
# x is guaranteed to be a non-negative integer.
#
#
#
# Example 1:
#
# Input: 4
# Output: 2
#
#
#
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since we want to return an integer, the decimal part will be truncated.
#
#


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        
        def guess(y):
            
            if y*y <= x:
                return True
            else:
                return False
    
        L = 0; R = x; ans = -1
        while L <= R:
            mid = (L+R)/2
            if guess(mid) == True:
                ans = mid
                L = mid + 1
            else:
                R = mid - 1
        
        return ans
        
        
        """
        def guess(x, y):
            return long(x)*x <= y
        
        y = x
        if y < 0: return 0
        
        L = 0
        R = y
        ans = 0
        while L <= R:
            mid = (L+R)/2
            if (guess(mid, y)):
                ans = mid
                L = mid + 1
            else:
                R = mid - 1
        
        return ans
        """
        
        
        
