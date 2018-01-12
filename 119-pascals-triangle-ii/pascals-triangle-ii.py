# -*- coding:utf-8 -*-


# Given an index k, return the kth row of the Pascal's triangle.
#
#
# For example, given k = 3,
# Return [1,3,3,1].
#
#
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        
        list = []
        
        for i in range(0, rowIndex+1):
            list.insert(0, 1)
            for j in range(1, len(list)-1):
                list[j] += list[j+1]
        
        return list
