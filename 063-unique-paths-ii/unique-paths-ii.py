# -*- coding:utf-8 -*-


# Follow up for "Unique Paths":
#
# Now consider if some obstacles are added to the grids. How many unique paths would there be?
#
# An obstacle and empty space is marked as 1 and 0 respectively in the grid.
#
# For example,
# There is one obstacle in the middle of a 3x3 grid as illustrated below.
#
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
#
# The total number of unique paths is 2.
#
# Note: m and n will be at most 100.


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        m = len(obstacleGrid)
        if m == 0: return 0
        n = len(obstacleGrid[0])
        if n == 0: return 0
        
        DP = [0 for j in range(0, n)]
        DP[0] = 1
        # DP[0] = 1 - obstacleGrid[0][0]
        # init the first row
        # for j in range(1, n):
            # if obstacleGrid[0][j] == 1:
                # DP[j] = 0
            # else:
                # DP[j] = DP[j-1]
        
        for i in range(0, m):
            for j in range(0, n):
                if obstacleGrid[i][j] == 1: # two purpose !!!
                    DP[j] = 0
                # else:
                elif j>0:
                    DP[j] = DP[j-1] + DP[j]      
                
                
                # if j == 0:
                    # if obstacleGrid[i][0] == 1:
                        # DP[j] = 0
                # else:
                    # if obstacleGrid[i][j] == 1:
                        # DP[j] = 0
                    # else:
                        # DP[j] = DP[j-1] + DP[j]
        
        return DP[n-1]
