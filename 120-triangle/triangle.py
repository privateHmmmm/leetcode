# -*- coding:utf-8 -*-


# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
#
# For example, given the following triangle
#
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
#
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#


class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        
        if not triangle:
            return 0
        
#         lists=triangle[0]      
#         for i in range(1, len(triangle)):
#             pre = lists[0]
#             for j in range(0, i + 1):
#                 cur = lists[j] if j < i else 0
#                 if j < i:
#                     lists[j] = triangle[i][j] + min(pre, lists[j])
#                 else:
#                     lists.append(triangle[i][j]+pre)
#                 pre = cur

#         return min(lists)

        res = [0 for i in range(0, len(triangle)+1)]
    
        for i in range(len(triangle)-1, -1, -1):
            for j in range(0, len(triangle[i])):
                res[j] = min(res[j], res[j+1])+triangle[i][j]
        
        return res[0]
             
