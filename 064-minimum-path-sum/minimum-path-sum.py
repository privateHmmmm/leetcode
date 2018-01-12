# -*- coding:utf-8 -*-


# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
#
# Note: You can only move either down or right at any point in time.
#
# Example 1:
#
# [[1,3,1],
#  [1,5,1],
#  [4,2,1]]
#
# Given the above grid map, return 7. Because the path 1&rarr;3&rarr;1&rarr;1&rarr;1 minimizes the sum.
#


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j != 0: grid[i][j] += grid[i][j-1]
                if j == 0 and i != 0: grid[i][j] += grid[i-1][j]
                if i !=0 and j != 0: grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        
        return grid[m-1][n-1]
            
