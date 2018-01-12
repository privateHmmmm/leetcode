# -*- coding:utf-8 -*-


# In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins. 
#
# What if we change the game so that players cannot re-use integers? 
#
# For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.
#
# Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally. 
#
# You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
#
#
# Example
#
# Input:
# maxChoosableInteger = 10
# desiredTotal = 11
#
# Output:
# false
#
# Explanation:
# No matter which integer the first player choose, the first player will lose.
# The first player can choose an integer from 1 up to 10.
# If the first player choose 1, the second player can only choose integers from 2 up to 10.
# The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
# Same with other integers chosen by the first player, the second player will always win.
#
#


import math
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        
        def Win(mask, map, desiredTotal):
            
            if mask in map:
                return map[mask]
            
            
            # Max = lists[int(math.log(mask-mask/2, 2))]
            
            # """
            Max = 0 
            for i in range(maxChoosableInteger-1, -1, -1):
                used = (mask >>i)&1
                if not used:
                    Max = max(Max, i+1)
                    break
                    
            if Max >= desiredTotal:
                map[mask] = True
                return True
            # """
            
            for i in range(0, maxChoosableInteger):
                cur = 1<<i
                if mask & cur == 0: 
                    # mask |= cur
                    if False == Win(mask ^ cur, map, desiredTotal-(i+1)):
                        # mask ^= cur
                        map[mask] = True
                        return True
                    # mask ^= cur
            
            map[mask] = False
            return False
        
        if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
            return False
        mask = 0
        map = {}
        return Win(mask, map, desiredTotal)
          
