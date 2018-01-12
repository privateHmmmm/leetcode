# -*- coding:utf-8 -*-


#
# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1: 
# Input:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
# Output:
#
# 0 0 0
# 0 1 0
# 0 0 0
#
#
#
# Example 2: 
# Input:
#
# 0 0 0
# 0 1 0
# 1 1 1
#
# Output:
#
# 0 0 0
# 0 1 0
# 1 2 1
#
#
#
# Note:
#
# The number of elements of the given matrix will not exceed 10,000.
# There are at least one 0 in the given matrix.
# The cells are adjacent in only four directions: up, down, left and right.
#
#
#


class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        """
        if not matrix:
            return []
        
        row = len(matrix)
        col = len(matrix[0])
        
        queue = []
        for i in range(0, row):
            for j in range(0, col):
                if matrix[i][j] == 0:
                    queue.append([i, j])
                else:
                    matrix[i][j] = 10000
        
        while queue:
            i, j = queue.pop()
            for s in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                newI = i+s[0]
                newJ = j+s[1]
                if newI<0 or newI>=row or newJ<0 or newJ>=col or matrix[newI][newJ] < matrix[i][j]+1:
                    continue
                matrix[newI][newJ] = matrix[i][j]+1
                queue.append([newI, newJ])
            
        return matrix
        """
        
        
        q, m, n = [], len(matrix), len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] != 0:
                    matrix[i][j] = 0x7fffffff
                else:
                    q.append((i, j))
        for i, j in q:
            for r, c in ((i, 1+j), (i, j-1), (i+1, j), (i-1, j)):
                z = matrix[i][j] + 1
                if 0 <= r < m and 0 <= c < n and matrix[r][c] > z:
                    matrix[r][c] = z
                    q.append((r, c))
        return matrix
    
    
