# -*- coding:utf-8 -*-


# Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.
#
#
# For example, given the range [5, 7], you should return 4.
#
#
# Credits:Special thanks to @amrsaqr for adding this problem and creating all test cases.


class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        """
        def HasEvenNum(min, max):
            if max!=min:
                return True
            else:
                if min % 2 == 0:
                    return True
                else:
                    return False
        
        res=0
        lens=0
        while n or m:
            if HasEvenNum(m,n) == False:
                res=(1<<lens)+res
            lens+=1
            
            m=m/2
            n=n/2
        return res
        """
        
        while n > m:
            n &= (n-1)
        return n & m
    
            
            
            
            
            
