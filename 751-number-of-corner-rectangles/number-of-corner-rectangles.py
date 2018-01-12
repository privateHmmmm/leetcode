# -*- coding:utf-8 -*-


#
# Given a grid where each entry is only 0 or 1, find the number of corner rectangles.
#
# A corner rectangle is 4 distinct 1s on the grid that form an axis-aligned rectangle.  Note that only the corners need to have the value 1.  Also, all four 1s used must be distinct.
#
#
# Example 1:
#
# Input: grid = 
# [[1, 0, 0, 1, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [1, 0, 1, 0, 1]]
# Output: 1
# Explanation: There is only one corner rectangle, with corners grid[1][2], grid[1][4], grid[3][2], grid[3][4].
#
#
#
# Example 2:
#
# Input: grid = 
# [[1, 1, 1],
#  [1, 1, 1],
#  [1, 1, 1]]
# Output: 9
# Explanation: There are four 2x2 rectangles, four 2x3 and 3x2 rectangles, and one 3x3 rectangle.
#
#
#
# Example 3:
#
# Input: grid = 
# [[1, 1, 1, 1]]
# Output: 0
# Explanation: Rectangles must have four distinct corners.
#
#
#
# Note:
#
# The number of rows and columns of grid will each be in the range [1, 200].
# Each grid[i][j] will be either 0 or 1.
# The number of 1s in the grid will be at most 6000.
#
#


import numpy as np
import itertools

class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
#         m = len(grid)
#         n = len(grid[0])
#         res = 0
        
#         for r1 in range(0, m):
#             for r2 in range(r1+1, m):
#                 count = 0
#                 for j in range(0, n):
#                     count += (grid[r1][j] and grid[r2][j])
#                 if count > 0:
#                     res += (count)*(count-1)/2
        
#         return res

        m = np.array(grid)
        counter = 0
        for (y0,y1) in itertools.combinations(m,2):  # 所有两两行向量的组合
            ones = np.dot(y0, y1)  # 点乘
            counter += ones*(ones-1)/2
        return int(counter)
