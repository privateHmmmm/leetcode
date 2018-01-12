# -*- coding:utf-8 -*-


# Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
#
# For example,
# Given n = 3,
#
# You should return the following matrix:
#
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]
#


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        
        if n == 0: return []
        
        matrix = [[0 for i in range(0, n)] for i in range(0, n)]
        rowBegin, rowEnd = 0, n-1
        colBegin, colEnd = 0, n-1
        now = 1
        while rowBegin<=rowEnd and colBegin<=colEnd:
            for j in range(colBegin, colEnd+1):
                matrix[rowBegin][j] = now
                now +=1
            rowBegin +=1
            
            for i in range(rowBegin, rowEnd+1):
                matrix[i][colEnd] = now
                now +=1
            colEnd -=1
            
            if rowBegin<=rowEnd:  # line 26 and 33 can be omitted, because matrix is a square
                for j in range(colEnd, colBegin-1, -1):
                    matrix[rowEnd][j] = now
                    now +=1
                rowEnd -=1
            
            if colBegin<=colEnd:
                for i in range(rowEnd, rowBegin-1, -1):
                    matrix[i][colBegin] = now
                    now +=1
                colBegin +=1
            
        return matrix
                    
