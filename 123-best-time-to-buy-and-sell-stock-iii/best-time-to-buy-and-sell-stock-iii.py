# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        buy1, buy2 = -2**31, -2**31
        sell1, sell2 = 0, 0
        
        for price in prices:
            sell2 = max(sell2, buy2+price)
            buy2 = max(buy2, sell1-price)
            sell1 = max(sell1, buy1+price)
            buy1 = max(buy1, -price)
        
        return sell2
        
