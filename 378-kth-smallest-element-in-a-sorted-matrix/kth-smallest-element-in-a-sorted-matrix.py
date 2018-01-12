# -*- coding:utf-8 -*-


# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
#
#
# Note: 
# You may assume k is always valid, 1 &le; k &le; n2.


from heapq import *
class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        
        def count(target):
            
            # the number that is less than target
            # O(2*n)
            res = 0
            i, j = 0, n-1
            while i <= n-1 and j >= 0:
                if matrix[i][j] < target:
                    res += (j+1) 
                    i += 1
                else:
                    # matrix[i][j] >= target
                    j -= 1
            
            return res
        
        n = len(matrix)
        L = matrix[0][0]
        R = matrix[n-1][n-1]
        
        while L < R-1:
            mid = (L+R)/2
            cnt = count(mid)
            if cnt < k:
                L = mid 
            else:
                R = mid - 1
            
        if count(R) < k: return R 
        return L
        
        """
        # Priority Queue
        # 1 -> 10 -> 12
        # 5 -> 11 -> 13
        # 9 -> 13 -> 15
        
        m = len(matrix)
        hq = []
        for j in range(0, m):
            heappush(hq, [matrix[0][j], 0, j])
        
        for i in range(0, k-1):
            tmp = heappop(hq)
            if tmp[1] < m-1:
                heappush(hq, [matrix[tmp[1]+1][tmp[2]], tmp[1]+1, tmp[2]])
        
        return heappop(hq)[0]
        """
        
