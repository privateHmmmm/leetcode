# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        """
        prices.append(-1)
        profit=0
        buy=-1

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                if buy == -1:
                    buy = prices[i-1]
            else:
                if buy != -1:
                    sell = prices[i-1]
                    profit+=(sell-buy)
                    buy = -1
                    
        return profit
        """
        
        res=0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                res += prices[i]-prices[i-1]
        return res
    
