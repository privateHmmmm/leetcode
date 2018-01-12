# -*- coding:utf-8 -*-


# Implement wildcard pattern matching with support for '?' and '*'.
#
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
#
# The matching should cover the entire input string (not partial).
#
# The function prototype should be:
# bool isMatch(const char *s, const char *p)
#
# Some examples:
# isMatch("aa","a") &rarr; false
# isMatch("aa","aa") &rarr; true
# isMatch("aaa","aa") &rarr; false
# isMatch("aa", "*") &rarr; true
# isMatch("aa", "a*") &rarr; true
# isMatch("ab", "?*") &rarr; true
# isMatch("aab", "c*a*b") &rarr; false
#


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        star = -1
        match = 0
        pp, sp = 0, 0
        while sp < len(s):
            if pp < len(p) and (p[pp] == s[sp] or p[pp] == '?'):
                sp +=1
                pp +=1
            elif pp < len(p) and p[pp] == '*':
                star = pp
                match = sp
                pp +=1 
            elif star != -1:
                match +=1
                sp = match
                pp = star + 1
            else:
                return False
        
        while pp < len(p):
            if p[pp] != '*': return False
            pp +=1
        
        return True
                
