# -*- coding:utf-8 -*-


# A sequence of number is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
#
# For example, these are arithmetic sequence:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
#
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
#
#
# A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.
#
# A slice (P, Q) of array A is called arithmetic if the sequence:
#     A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.
#
# The function should return the number of arithmetic slices in the array A. 
#
#
# Example:
#
# A = [1, 2, 3, 4]
#
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
#


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
        # array          num     与上一组比较      
        # 1 2 3           1        1 - 0 = 1
        # 1 2 3 4         3        3 - 1 = 2
        # 1 2 3 4 5       6        6 - 3 = 3
        # 1 2 3 4 5 6     10       10 - 6 = 4
        
        
        res = 0
        addend = 0
        
        for i in range(2, len(A)):
            if A[i-1]-A[i] == A[i-2] - A[i-1]:
                addend += 1
                res += addend
            else:
                addend = 0
        
        return res
                
