# -*- coding:utf-8 -*-


#
# Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, where in each step you can delete one character in either string.
#
#
# Example 1:
#
# Input: "sea", "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
#
#
#
# Note:
#
# The length of given words won't exceed 500.
# Characters in given words can only be lower-case letters.
#
#


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        DP = [[0 for j in range(len(word2)+1)] for i in range(0, len(word1)+1)]
        
        for i in range(0, len(word1)+1):
            for j in range(0, len(word2)+1):
                # if i == 0 or j == 0:
                    # DP[i][j] = 0
                # else:
                if i and j:
                    DP[i][j] = DP[i-1][j-1] + 1 if word1[i-1] == word2[j-1] else max(DP[i-1][j], DP[i][j-1])
        
        return len(word1)+len(word2) - DP[len(word1)][len(word2)]*2
                                                             
