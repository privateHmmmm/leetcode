# -*- coding:utf-8 -*-


# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
#
# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
#
# How many possible unique paths are there?
#
#
#
# Above is a 3 x 7 grid. How many possible unique paths are there?
#
#
# Note: m and n will be at most 100.


class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        DP = [0 for j in range(0, n)] 
        DP[0] = 1
        
        for i in range(0, m):
            for j in range(1, n):
                DP[j] = DP[j-1] + DP[j]
            
        return DP[n-1]
        
