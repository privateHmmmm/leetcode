# -*- coding:utf-8 -*-


# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:Special thanks to @Freezen for adding this problem and creating all test cases.


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        
        lens = len(prices)
        if lens <= 1: return 0

        if k >= lens/2:
            # quick solution
            profit = 0
            for i in range(1, lens):
                if prices[i] > prices[i-1]:
                    profit += (prices[i]-prices[i-1])
            return profit
            
        DP = [[0 for j in range(0, lens)] for i in range(0, k+1)]

        # DP[i][j] is the max profit for up to i transactions by time j (0<=i<=k, 0<=j<len(prices)).
        for i in range(1, k + 1):
            tmpMax = -prices[0]  
            for j in range(1, lens):
                DP[i][j] = max(DP[i][j-1], tmpMax + prices[j])
                tmpMax = max(tmpMax, DP[i-1][j-1] - prices[j])

        return DP[k][lens - 1]
        
