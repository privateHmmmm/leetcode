# -*- coding:utf-8 -*-


# Given a roman numeral, convert it to an integer.
#
# Input is guaranteed to be within the range from 1 to 3999.


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        # z = 0
        # for i in range(0, len(s) - 1):
        #     if roman[s[i]] < roman[s[i+1]]:
        #         z -= roman[s[i]]
        #     else:
        #         z += roman[s[i]]
        # return z + roman[s[-1]]
    
        
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        z = 0
        for i in range(0, len(s)):
            z += roman[s[i]]
        
        if s.find("IV") >= 0:
            z -= 2
        if s.find("IX") >= 0:
            z -= 2
        if s.find("XL") >= 0:
            z -= 20
        if s.find("XC") >= 0:
            z -= 20
        if s.find("CD") >= 0:
            z -= 200
        if s.find("CM") >= 0:
            z -= 200
        return z
            
