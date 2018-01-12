# -*- coding:utf-8 -*-


#
# Given a string S and a string T, count the number of distinct subsequences of S which equals T.
#
#
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
#
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
#
# Return 3.
#


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        
        DP=[[1 for i in range(len(s)+1)] for j in range(0, len(t)+1)]
        
        for j in range(1, len(t)+1):
            for i in range(0, len(s)+1):
                if i == 0:
                    DP[j][0]=0
                else:
                    if s[i-1]==t[j-1]:
                        DP[j][i]=DP[j-1][i-1]+DP[j][i-1]
                    else:
                        DP[j][i]=DP[j][i-1]
        
        return DP[len(t)][len(s)]
        
        
