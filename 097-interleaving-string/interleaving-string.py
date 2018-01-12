# -*- coding:utf-8 -*-


#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
#
#
#
# For example,
# Given:
# s1 = "aabcc",
# s2 = "dbbca",
#
#
# When s3 = "aadbbcbcac", return true.
# When s3 = "aadbbbaccc", return false.
#


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        
        if s1 == "": return s2 == s3
        if s2 == "": return s1 == s3
        if len(s1) + len(s2) != len(s3): return False
        
        DP = [[False for j in range(0, len(s2)+1)] for i in range(0, len(s1)+1)]

        for j in range(0, len(s2)+1):
            if s3[0:j] == s2[0:j]: DP[0][j] = True
        
        for i in range(0, len(s1)+1):
            if s3[0:i] == s1[0:i]: DP[i][0] = True
        
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                lens = i + j 
                DP[i][j] = (DP[i-1][j] and s3[lens-1] == s1[i-1]) or \
                            (DP[i][j-1] and s3[lens-1] == s2[j-1])
               
        return DP[len(s1)][len(s2)]
        
