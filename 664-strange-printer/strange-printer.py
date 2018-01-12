# -*- coding:utf-8 -*-


#
# There is a strange printer with the following two special requirements:
#
#
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
#
#
#
#
#
# Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.
#
#
# Example 1:
#
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
#
#
#
# Example 2:
#
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
#
#
#
# Hint: Length of the given string will not exceed 100.


class Solution(object):
    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # DP[i][j] = min(DP[i][k]+DP[k+1][j-1]) if s[k] == s[j]
        # k 到 j开始全部赋值为s[k]
        if not s: return 0
        m = len(s)
        DP = [[0 for i in range(0, m)] for j in range(0, m)]
        
        for i in range(0, m):
            DP[i][i] = 1
        
        for l in range(2, m+1):
            for i in range(0, m+1-l):
                j = i+l-1
                DP[i][j] = DP[i][j-1] + 1
                for k in range(i, j):
                    if s[k] == s[j]:
                        DP[i][j] = min(DP[i][j], DP[i][k]+DP[k+1][j-1])
        
        return DP[0][m-1]                        
                        
