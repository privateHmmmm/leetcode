# -*- coding:utf-8 -*-


# Implement regular expression matching with support for '.' and '*'.
#
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
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
# isMatch("aa", "a*") &rarr; true
# isMatch("aa", ".*") &rarr; true
# isMatch("ab", ".*") &rarr; true
# isMatch("aab", "c*a*b") &rarr; true
#


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        """
             X  0  1  2  3 (S)
             "" a  b  a  a
        X "" T  F  F  F  F
        0 a  F  
        1 b  F
        2 .  F
        3 *  T
      (P)
       """
        
        DP = [[False for j in range(0, len(s)+1)] for i in range(0, len(p)+1)]
        
        DP[0][0] = True
        # DP[0][j] = False
        for i in range(0, len(p)):
            if p[i] == '*':  # '*' before must have a character
                DP[i+1][0] = DP[i-1][0]   # match zero preceding character
        
        for i in range(0, len(p)):
            for j in range(0, len(s)):
                if p[i] == '.' or p[i] == s[j]:
                    DP[i+1][j+1] = DP[i][j]
                elif p[i] == '*':
                    # match zero, one, more p[i-1] 
                    DP[i+1][j+1] = DP[i-1][j+1] or ((p[i-1] == s[j] or p[i-1] == '.') and (DP[i][j+1] or DP[i+1][j]))
                    
        return DP[len(p)][len(s)]
                    
