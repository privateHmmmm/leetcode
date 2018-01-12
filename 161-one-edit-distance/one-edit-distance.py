# -*- coding:utf-8 -*-


# Given two strings S and T, determine if they are both one edit distance apart.


class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        # if s == t: return False
        if abs(len(s)-len(t)) >= 2: return False
        
        i = 0
        while i < min(len(s), len(t)):
            if s[i] != t[i]:
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                elif len(s) > len(t):
                    return s[i+1:] == t[i:]
                else:
                    return s[i:] == t[i+1:]
            i += 1
    
        return abs(len(s[i:]) - len(t[i:])) == 1
        
