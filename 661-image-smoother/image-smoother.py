# -*- coding:utf-8 -*-


# Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself.  If a cell has less than 8 surrounding cells, then use as many as you can.
#
# Example 1:
#
# Input:
# [[1,1,1],
#  [1,0,1],
#  [1,1,1]]
# Output:
# [[0, 0, 0],
#  [0, 0, 0],
#  [0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
#
#
#
# Note:
#
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
#
#


class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not M:
            return None
        
        row=len(M)
        col=len(M[0])
        
        N=[[0 for j in range(col)] for i in range(row)]
        
        for i in range(0, row):
            for j in range(0, col):
                tmp=0
                cnt = 0
                step=[(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]
                for s in step:
                    newI=i+s[0]
                    newJ=j+s[1]
                    if newI>=0 and newI<row and newJ>=0 and newJ<col:
                        cnt += 1
                        tmp += M[newI][newJ]
                        
                N[i][j]=tmp/cnt
        
        return N
        
