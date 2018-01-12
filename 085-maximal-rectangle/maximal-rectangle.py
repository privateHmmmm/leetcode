# -*- coding:utf-8 -*-


#
# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
#
# Return 6.
#


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        
        # height
        # 1  0  1  0  0
        # 2  0  2  1  1
        # 3  1  3  2  2
        # 4  0  0  3  0
        
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        if n == 0: return 0
        
        res = 0
        height = [0] * (n+1)

        for i in range(0, m):
            for j in range(0, n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            
            stack = []
            for j in range(0, n+1):
                while stack and height[stack[-1]] > height[j]:
                    h = height[stack.pop()]
                    lens = j - (stack[-1] if stack else -1) - 1
                    res = max(res, h*lens)
                stack.append(j)
        
        return res
                
