# -*- coding:utf-8 -*-


#
# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
#
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
#
#
# For example,
# Given encoded message "12",
# it could be decoded as "AB" (1 2) or "L" (12).
#
#
#
# The number of ways decoding "12" is 2.
#


class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        """
        if s == "": return 0
        
        DP = [0 for i in range(0, len(s)+1)]
        DP[0] = 1
        
        for i in range(1, len(s)+1):
            if 1<=int(s[i-1])<=9:
                DP[i] += DP[i-1]
            if i >= 2 and (10<=int(s[i-2:i])<=26):
                DP[i] += DP[i-2]
        
        return DP[-1]
        """
    
        # space: O(1)
        if s == "": return 0
        
        c1 = 1
        c2 = 1 if 1<=int(s[0])<=9 else 0
        
        for i in range(2, len(s)+1):
            c3 = 0
            if 1 <= int(s[i-1]) <= 9:
                c3 += c2
            if (10 <= int(s[i-2:i]) <= 26):
                c3 += c1
            c1, c2 = c2, c3
            
        return c2
