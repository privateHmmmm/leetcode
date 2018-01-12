# -*- coding:utf-8 -*-


# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), return the maximum enemies you can kill using one bomb. The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since the wall is too strong to be destroyed.
#  Note that you can only put the bomb at an empty cell. 
#
# Example:
#
# For the given grid
#
# 0 E 0 0
# E 0 W E
# 0 E 0 0
#
# return 3. (Placing a bomb at (1,1) kills 3 enemies)
#
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating all test cases.


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        if n == 0: return 0
        
        res = 0
        rowKill = 0
        colKill = [0 for i in range(0, n)]
        
        for i in range(0, m):
            for j in range(0, n):
                if j == 0 or grid[i][j-1] == 'W':
                    rowKill = 0
                    for k in range(j, n):
                        if grid[i][k] != 'W':
                            if grid[i][k] == 'E':
                                rowKill += 1
                            k += 1
                        else:
                            break
                if i == 0 or grid[i-1][j] == 'W':
                    colKill[j] = 0
                    for k in range(i, m):
                        if grid[k][j] != 'W':
                            if grid[k][j] == 'E':
                                colKill[j] += 1
                            k += 1
                        else:
                            break
                if grid[i][j] == '0':
                    res = max(res, rowKill + colKill[j])
        return res
                    
