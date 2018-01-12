# -*- coding:utf-8 -*-


#
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
#
#
#
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
#
#
#
# Example 2:
# coins = [2], amount = 3
# return -1.
#
#
#
# Note:
# You may assume that you have an infinite number of each kind of coin.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        
        # """
        # coins.sort(reverse=True)
        DP = [-1 for i in range(0, amount+1)]
        DP[0] = 0
        
        n = 1
        while n <= amount:
            for coin in coins:
                if coin>n:
                    continue
                elif coin == n:
                    DP[n] = 1
                    break
                else:
                    if DP[n-coin] != -1 and (DP[n] == -1 or DP[n-coin]+1 < DP[n]):
                        DP[n] = DP[n-coin]+1
            
            n+=1
        
        return DP[amount]
        # """
        """
        # DP[idx][amount] = DP[idx-1][amount], DP[idx-1][amount-coins[idx]]+1, DP[idx-1][amount-2*coins[idx]]+2, ...
        
        # coins.sort(reverse=True)
        DP = [[-1 for j in range(0, amount+1)] for i in range(0, 2)]
        # need to init the first row element, first column 
        DP[0][0] = 0
        DP[1][0] = 0
        
        for idx in range(1, len(coins)+1):
            for money in range(1, amount+1):
                DP[idx%2][money] = DP[(idx-1)%2][money]
                if money>=coins[idx-1] and DP[idx%2][money-coins[idx-1]] != -1:
                    tmp = DP[idx%2][money-coins[idx-1]]+1
                    if DP[idx%2][money]==-1 or tmp<DP[idx%2][money]:
                        DP[idx%2][money] = tmp
        # print DP  
        return DP[len(coins)%2][amount]
        """
                
