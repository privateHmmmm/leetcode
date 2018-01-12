# -*- coding:utf-8 -*-


# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
#
# Example 1:
#
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
#
#
#
# Example 2:
#
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
#
#
#
# Note:
# 0 < s1.length, s2.length <= 1000.
# All elements of each string will have an ASCII value in [97, 122]. 
#


class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        DP = [[0 for j in range(0, len(s2)+1)] for i in range(len(s1)+1)]
        
        for i in range(0, len(s1)):
            DP[i+1][0] = ord(s1[i]) + DP[i][0]
        
        for j in range(0, len(s2)):
            DP[0][j+1] = ord(s2[j]) + DP[0][j]
        
        for i in range(0, len(s1)):
            for j in range(0, len(s2)):
                DP[i+1][j+1] = min(DP[i][j+1]+ord(s1[i]), DP[i+1][j]+ord(s2[j]))
                if s1[i] == s2[j]:
                    DP[i+1][j+1] = min(DP[i][j], DP[i+1][j+1])
        
        # print DP
        return DP[len(s1)][len(s2)]
    
