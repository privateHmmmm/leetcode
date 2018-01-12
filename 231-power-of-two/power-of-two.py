# -*- coding:utf-8 -*-


#
# Given an integer, write a function to determine if it is a power of two.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        """
        if n <=0:
            return False
        
        lens=len(str(n))
        
        for i in range(0, 10*((lens+1)/2)):
            if i*i == n:
                return True
            elif i*i > n:
                return False
                
        return False
        """
        
        if n <= 0:
            return False
        
        while n !=1:
            if n % 2 != 0:
                return False
            else:
                n =n/2
        
        return True
