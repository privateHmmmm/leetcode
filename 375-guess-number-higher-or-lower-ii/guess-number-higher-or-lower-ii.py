# -*- coding:utf-8 -*-


# We are playing the Guess Game. The game is as follows: 
#
# I pick a number from 1 to n. You have to guess which number I picked.
#
# Every time you guess wrong, I'll tell you whether the number I picked is higher or lower. 
#
# However, when you guess a particular number x,  and you guess wrong, you pay $x. You win the game when you guess the number I picked.
#
#
# Example:
#
# n = 10, I pick 8.
#
# First round:  You guess 5, I tell you that it's higher. You pay $5.
# Second round: You guess 7, I tell you that it's higher. You pay $7.
# Third round:  You guess 9, I tell you that it's lower. You pay $9.
#
# Game over. 8 is the number I picked.
#
# You end up paying $5 + $7 + $9 = $21.
#
#
#
# Given a particular n &ge; 1, find out how much money you need to have to guarantee a win.
#
# Credits:Special thanks to @agave and @StefanPochmann for adding this problem and creating all test cases.


class Solution(object):
    def getMoneyAmount(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        DP = [[0 for i in range(n)] for j in range(n)]
        # DP[i][i] = 0
        
        for lens in range(2, n+1):
            for i in range(0, n+1-lens):
                j = i+lens-1
                global_min = min((i+1)+DP[i+1][j], (j+1)+DP[i][j-1])
                for k in range(i+1, j):
                    local_max = (k+1) + max(DP[i][k-1], DP[k+1][j])
                    global_min= min(global_min, local_max)
                DP[i][j] = global_min
        
        return DP[0][n-1]
