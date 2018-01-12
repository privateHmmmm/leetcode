# -*- coding:utf-8 -*-


#
# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
#
#
#
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
#
#
#
# Note: You may assume that n is not less than 2 and not larger than 58.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        # My DP
        def multiply(l):
            
            if not l:
                return 1
            return reduce(lambda x, y: x*y, l)
        
        DP = [[i] for i in range(n+1)]
        DP[0] = []
        
        for i in range(2, n+1):
            Max = 1
            tmp_dp = []
            for j in range(i, i/2-1, -1):
                tmp = multiply(DP[j])*multiply(DP[i-j])
                if Max < tmp:
                    Max = tmp
                    tmp_dp = DP[j] + DP[i-j]
            
            DP[i][:] = tmp_dp
            
        Max = 1
        for j in range(1, n/2+1, 1):
            Max = max(Max, multiply(DP[j])*multiply(DP[n-j]))
        
        return Max
        """ 
        
        if n == 2 or n == 3:
            return n-1
        if not n % 3:
            return 3**(n / 3) 
        elif n % 3 == 1:
            return 3**((n / 3) - 1)*4
        else:
            return 3**(n / 3) * 2
        
        
        
    
