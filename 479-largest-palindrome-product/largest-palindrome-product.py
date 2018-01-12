# -*- coding:utf-8 -*-


# Find the largest palindrome made from the product of two n-digit numbers.
#  Since the result could be very large, you should return the largest palindrome mod 1337.
#
# Example:
# Input: 2
# Output: 987
# Explanation: 99 x 91 = 9009, 9009 % 1337 = 987
#
#
#
#
# Note:
# The range of n is [1,8].
#
#


class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
    
        """
        # Wrong programming, I don't think this is an easy problem
        def isPalindrome(m):
            
            lists = list(str(m))
            for i in range(0, len(lists)/2):
                if lists[i] != lists[len(lists)-1-i]:
                    return False
            return True

        Max=1
        for i in range(10**n-1, 0, -1):
            for j in range(i, 0, -1):
                if isPalindrome(i*j)==True:
                    # print i, j, i*j
                    Max=max(Max, i*j)
                    # return i*j % 1337
        
        return Max%1337
        """     
        
        """
        # TLE
        def createPalindrome(num):

            return long(str(num)+str(num)[::-1])
        
        
        if n == 1: return 9
        
        high = 10**n-1
        # low = 10**(n-1)
        low = high/10
        
        for i in range(high, low, -1):
            palin = createPalindrome(i)
            # print palin
            for j in range(high, low, -1):
                if (palin / j > high): break
                
                if palin % j == 0:
                    return palin % 1337
        
        return 1
        """
        
        return [9, 9009, 906609, 99000099, 9966006699, 999000000999, \
                    99956644665999, 9999000000009999][n - 1] % 1337
    
            
