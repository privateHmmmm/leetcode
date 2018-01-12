# -*- coding:utf-8 -*-


#
# Given an Android 3x3 key lock screen and two integers m and n, where  1 &le; m &le; n &le; 9, count the total number of unlock patterns of the Android lock screen, which consist of minimum of m keys and maximum n keys.
#
# Rules for a valid pattern:
#
# Each pattern must connect at least m keys and at most n keys.
# All the keys must be distinct.
# If the line connecting two consecutive keys in the pattern passes through any other keys, the other keys must have previously selected in the pattern. No jumps through non selected key is allowed.
# The order of keys used matters.
#
#
#
#
#
# Explanation:
#
# | 1 | 2 | 3 |
# | 4 | 5 | 6 |
# | 7 | 8 | 9 |
#
#
#
# Invalid move: 4 - 1 - 3 - 6 
#
# Line  1 - 3 passes through key 2 which had not been selected in the pattern.
#
# Invalid move: 4 - 1 - 9 - 2
#
# Line  1 - 9 passes through key 5 which had not been selected in the pattern.
#
# Valid move: 2 - 4 - 1 - 3 - 6
#
# Line 1 - 3 is valid because it passes through key 2, which had been selected in the pattern
#
# Valid move: 6 - 5 - 4 - 1 - 9 - 2
#
# Line 1 - 9 is valid because it passes through key 5, which had been selected in the pattern.
#
# Example:
# Given m = 1, n = 1, return 9.
#
#
# Credits:Special thanks to @elmirap for adding this problem and creating all test cases.


class Solution(object):
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        skip = [[0 for i in range(0, 10)] for j in range(0, 10)]
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[7][9] = skip[9][7] = 8
        skip[3][9] = skip[9][3] = 6
        skip[1][9] = skip[9][1] = skip[3][7] = skip[7][3] = 5
        skip[4][6] = skip[6][4] = skip[2][8] = skip[8][2] = 5
        
        visited = [False for i in range(0, 10)]
        
        def DFS(cur, remain):
            
            res = 0
            if remain < 0: return 0
            if remain == 0: return 1
            
            visited[cur] = True
            for i in range(1, 10):
                if (not visited[i] and (skip[cur][i] == 0 or visited[skip[cur][i]])):
                    res += DFS(i, remain - 1)    
            
            visited[cur] = False
            return res
    
        res = 0
        for remain in range(m, n+1):
            res += DFS(1, remain-1) * 4
            res += DFS(2, remain-1) * 4
            res += DFS(5, remain-1)
        
        return res
