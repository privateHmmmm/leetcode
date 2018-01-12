# -*- coding:utf-8 -*-


#
# There are a row of n houses, each house can be painted with one of the k colors. The cost of painting each house with a certain color is different. You have to paint all the houses such that no two adjacent houses have the same color.
#
#
# The cost of painting each house with a certain color is represented by a n x k cost matrix. For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.
#
#
# Note:
# All costs are positive integers.
#
# Follow up:
# Could you solve it in O(nk) runtime?


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        
        # red blue green yellow ... 
        # 记录上一层 倒数第一小 和倒数第二小
        
        n = len(costs)
        if n == 0: return 0
        k = len(costs[0]) 
        if k == 0: return 0
        
        min1, min2 = -1, -1
        for i in range(0, n):
            last1, last2 = min1, min2
            min1, min2 = -1, -1
            for j in range(0, k):
                if j != last1:
                    costs[i][j] += (0 if last1 == -1 else costs[i-1][last1])
                else:
                    costs[i][j] += (0 if last2 == -1 else costs[i-1][last2])
                
                if min1 == -1 or costs[i][j] < costs[i][min1]:
                    min2 = min1
                    min1 = j
                elif min2 == -1 or costs[i][j] < costs[i][min2]:
                    min2 = j
          
        return costs[n-1][min1]
                    
