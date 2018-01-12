# -*- coding:utf-8 -*-


#
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        palindrome = [[False for i in range(len(s))] for j in range(0, len(s))]
        
        for i in range(0, len(s)):
            palindrome[i][i] = True
        
        for r in range(2, len(s)+1):
            for i in range(0, len(s)+1-r):
                j = i+r-1
                if r == 2:
                    if s[i] == s[j]: palindrome[i][j] = True
                else:
                    if s[i] == s[j] and palindrome[i+1][j-1] == True: palindrome[i][j] = True
                        
        _min = [len(s)-1 for i in range(0, len(s))]
        
        for i in range(0, len(s)):
            for j in range(0, i+1):
                if palindrome[j][i] == True:
                    if j == 0:
                        _min[i] = 0
                    else:
                        _min[i] = min(_min[i], _min[j-1]+1)
        
        return _min[len(s)-1]
    
