# -*- coding:utf-8 -*-


# Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
# You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
# Return the maximum profit you can make.
#
# Example 1:
#
# Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
# Output: 8
# Explanation: The maximum profit can be achieved by:
# Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
#
#
#
# Note:
# 0 < prices.length <= 50000.
# 0 < prices[i] < 50000.
# 0 <= fee < 50000.
#


class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        
        # (x2-x1)+(x4-x3)=(x4-x1)+(x2-x3) because x2>x3, so (x2-x1)+(x4-x3) > (x4-x1) is true always
        # Let (x2-x1)+(x4-x3)-2*fee>(x4-x1)-fee -->x2-x3>fee
        
        if len(prices) <= 1: return 0
        
        DP = [0 for i in range(0, len(prices))]
        DP[0] = 0
        DP[1] = 0 if prices[1] - prices[0] - fee <= 0 else prices[1] - prices[0] - fee
        
        tmp_max = prices[1] - prices[0] -fee
        for i in range(2, len(prices)):
            tmp_max = max(tmp_max + prices[i] - prices[i-1], 
                          DP[i-2] + prices[i] - prices[i-1] - fee)
            DP[i] = max(DP[i-1], tmp_max)
            # print i, tmp_max, DP[i]
        
        # print DP
        return DP[-1]
        
