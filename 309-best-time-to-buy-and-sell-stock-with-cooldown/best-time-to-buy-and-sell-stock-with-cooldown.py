# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like
# (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
#
#
#     You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#     After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
#
#
# Example:
#
# prices = [1, 2, 3, 0, 2]
# maxProfit = 3
# transactions = [buy, sell, cooldown, buy, sell]
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        # buy[i] means before day i what is the maxProfit for any sequence end with buy.
        # sell[i]means before day i what is the maxProfit for any sequence end with sell.
        # cooldown[i]: means before day i what is the maxProfit for any sequence end with cooldown.
        # buy[i] = max(buy[i-1], cooldown[i-1] - prices[i]
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        # cooldown[i] = max(cooldown[i-1], sell[i-1])
        # also we have cooldown[i-1] <= sell[i-1]
        # so cooldown[i] = sell[i-1]
        
        # now we have (or maybe we can think of this directly)
        # buy[i] = max(buy[i-1], sell[i-2]-prices[i])
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        
        # if len(prices) < 2: return 0
        buy, preBuy = -2**31, 0
        sell, preSell = 0, 0
        for i in range(0, len(prices)):
            preBuy = buy
            buy = max(preBuy, preSell-prices[i])
            preSell = sell
            sell = max(preSell, preBuy+prices[i])
        
        return sell
    
