# -*- coding:utf-8 -*-


# Given numRows, generate the first numRows of Pascal's triangle.
#
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
#
#


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        res = []
        tmp = []
        
        for i in range(0, numRows):
            tmp.insert(0, 1)
            for j in range(1, len(tmp)-1):
                tmp[j] = (tmp[j] + tmp[j+1])
            res.append(copy.copy(tmp))
        
        return res
    
