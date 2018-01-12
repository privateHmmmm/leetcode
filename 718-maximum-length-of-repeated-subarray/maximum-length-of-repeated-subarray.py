# -*- coding:utf-8 -*-


# Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.
#
# Example 1:
#
# Input:
# A: [1,2,3,2,1]
# B: [3,2,1,4,7]
# Output: 3
# Explanation: 
# The repeated subarray with maximum length is [3, 2, 1].
#
#
#
# Note:
#
# 1 <= len(A), len(B) <= 1000
# 0 <= A[i], B[i] < 100
#
#


class Solution(object):
    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
      
        DP = [[0 for j in range(len(B)+1)] for i in range(len(A)+1)]
       
        _max = 0
        for i in range(0, len(A)):
            for j in range(0, len(B)):
                if A[i] == B[j]:
                    DP[i+1][j+1] = DP[i][j] + 1
                    _max = max(_max, DP[i+1][j+1])
                # else:
                    # DP[i+1][j+1] = 0
        
        return _max
