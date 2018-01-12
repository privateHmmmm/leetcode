# -*- coding:utf-8 -*-


#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
#
#
# click to show follow up.
#
# Follow up:
#
#
# Did you use extra space?
# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
#
#


class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        if matrix == []:
            return
        
        row = len(matrix)
        column = len(matrix[0])
        col0 = 1
        
        for i in range(0, row):
            for j in range(0, column):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        col0 = 0
                    else:
                        matrix[0][j] = 0
    
        for i in range(row-1, -1, -1):
            for j in range(column-1, -1, -1):
                if j == 0:
                    if matrix[i][0] == 0 or col0 == 0:
                        matrix[i][j] = 0
                else:
                    if matrix[i][0] == 0 or matrix[0][j] == 0:
                        matrix[i][j] = 0
                    
        return
        
        
        
            
