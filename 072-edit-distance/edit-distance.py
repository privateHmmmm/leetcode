# -*- coding:utf-8 -*-


#
# Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
#
#
#
# You have the following 3 operations permitted on a word:
#
#
#
# a) Insert a character
# b) Delete a character
# c) Replace a character
#


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        l1=len(word1)
        l2=len(word2)
        
        DP=[[0 for j in range(0, l2+1)] for i in range(0, l1+1)]
        
        for i in range(0, l1+1):
            DP[i][0]=i
        
        for j in range(0, l2+1):
            DP[0][j]=j
        
        for i in range(1, l1+1):
            for j in range(1, l2+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j]=DP[i-1][j-1]
                else:
                    DP[i][j]=min(DP[i-1][j-1]+1, DP[i-1][j]+1, DP[i][j-1]+1)
                    
        return DP[l1][l2]
                
                
                
