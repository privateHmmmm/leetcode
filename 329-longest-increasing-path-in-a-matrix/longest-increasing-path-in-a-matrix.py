# -*- coding:utf-8 -*-


# Given an integer matrix, find the length of the longest increasing path.
#
#
# From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
#
#
# Example 1:
#
# nums = [
#   [9,9,4],
#   [6,6,8],
#   [2,1,1]
# ]
#
#
#
#
# Return 4
#
# The longest increasing path is [1, 2, 6, 9].
#
#
# Example 2:
#
# nums = [
#   [3,4,5],
#   [3,2,6],
#   [2,2,1]
# ]
#
#
#
#
# Return 4
#
# The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        n = len(matrix)
        if n == 0: return 0
        m = len(matrix[0])
        if m == 0: return 0
        
        DP = [[0 for j in range(0, m)] for i in range(0, n)]
        
        def robot(i, j):
            
            if DP[i][j] == 0:
                _max = 0
                for s in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    newI = i + s[0]
                    newJ = j + s[1]
                    if 0<=newI<n and 0<=newJ<m and matrix[newI][newJ] < matrix[i][j]:
                        _max = max(_max, robot(newI, newJ))
                DP[i][j] = _max + 1
            
            return DP[i][j]
                        
        ans = 0
        for i in range(0, n):
            for j in range(0, m):
                ans = max(ans, robot(i, j))
    
        return ans
        
