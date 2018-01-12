# -*- coding:utf-8 -*-


# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
#
#
#
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
#
#
#
#
# For example,
#
# Consider the following matrix:
#
#
# [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
#
#
# Given target = 3, return true.


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        
        L, R = 0, m*n-1
        while L<=R:
            mid = (R-L)/2 + L
            value = matrix[mid/n][mid%n]
            if target > value:
                L = mid + 1
            elif target == value:
                return True
            else:
                R = mid - 1
        
        return False
