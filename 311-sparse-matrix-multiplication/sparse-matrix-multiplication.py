# -*- coding:utf-8 -*-


# Given two sparse matrices A and B, return the result of AB.
#
# You may assume that A's column number is equal to B's row number.
#
# Example:
#
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
#
#
#      |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
# AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
#                   | 0 0 1 |
#


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        
        if not A or not B: return []
        
        row = len(A)
        col = len(B[0])
        res = [[0 for j in range(0, col)] for i in range(0, row)]
        
        for i in range(0, row):
            for k in range(0, len(A[0])):
                if A[i][k] != 0:
                    for j in range(0, col):
                        res[i][j] += A[i][k] * B[k][j]
        
        return res
        
