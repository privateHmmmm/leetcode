# -*- coding:utf-8 -*-


#
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
#
# For example,
# If n = 4 and k = 2, a solution is:
#
#
#
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]
#


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        
        # will TLE, I don't know why
        ans = []
        path = []
        
        def robot(idx, remain):
            
            if remain == 0:
                ans.append(copy.copy(path))
                return
            
            if remain > n-idx: return
            for i in range(idx, n):
                path.append(i+1)
                robot(i+1, remain-1)
                path.pop()
         
        robot(0, k)
        return ans
        
#         ans = []
#         path = [0 for i in range(0, k)]
        
#         def robot(idx, remain): # last element
            
#             if remain == 0:
#                 ans.append(copy.copy(path))
#                 return
            
#             for i in range(idx+1, n+1):
#                 path[k-remain] = i
#                 # remain -= 1  # No No No !!!
#                 robot(i, remain-1)

#         robot(0, k)
#         return ans
             
