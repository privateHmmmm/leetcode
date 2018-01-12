# -*- coding:utf-8 -*-


#
# There is a fence with n posts, each post can be painted with one of the k colors.
# You have to paint all the posts such that no more than two adjacent fence posts have the same color. 
# Return the total number of ways you can paint the fence. 
#
# Note:
# n and k are non-negative integers. 


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
        if n == 0: return 0
        # if n == 1: return k
        
        # total = k
        # same = total
        # diff = (k-1)*total
        
        same = 0
        diff = k
        
        for i in range(1, n):
            same, diff = diff, (k-1)*(same+diff)
            # same = diff
        return same+diff
