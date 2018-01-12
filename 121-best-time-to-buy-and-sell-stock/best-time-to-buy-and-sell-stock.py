# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
#
# Example 1:
#
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
#
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
#
#
#
# Example 2:
#
# Input: [7, 6, 4, 3, 1]
# Output: 0
#
# In this case, no transaction is done, i.e. max profit = 0.
#
#


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        if not prices: return 0
        tmp_max = 0
        DP = [0 for i in range(0, len(prices))]
        
        for i in range(1, len(prices)):
            tmp_max = tmp_max - prices[i-1] + prices[i]
            tmp_max = max(tmp_max, prices[i] - prices[i-1])
            DP[i] = max(DP[i-1], tmp_max)
        
        return max(DP)
        """
            
        if not prices: return 0
        _min = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            profit = max(profit, prices[i] - _min)
            _min = min(_min, prices[i])
        
        return profit
