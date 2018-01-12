# -*- coding:utf-8 -*-


#
#     Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
#     number on it represented by array nums.
#
#     You are asked to burst all the balloons. If the you burst
#     balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left
#     and right are adjacent indices of i. After the burst, the left and right
#     then becomes adjacent.
#
#
#     Find the maximum coins you can collect by bursting the balloons wisely.
#
#
#     Note: 
#     (1) You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
#     (2) 0 &le; n &le; 500, 0 &le; nums[i] &le; 100
#
#
#
#
#     Example:
#
#
#     Given [3, 1, 5, 8]
#
#
#     Return 167
#
#
#     nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
#    coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        nums = [1] + nums + [1]
        
        
        DP = [[0 for i in range(0, n+2)] for j in range(0, n+2)]  # maxCoin(nums[i:j+1])
        
        for l in range(1, n+1):
            for i in range(1, n+2-l):
                j = i + l - 1
                for k in range(i, j+1):
                    DP[i][j] = max(DP[i][j], DP[i][k-1] + nums[i-1]*nums[k]*nums[j+1] + DP[k+1][j])
        
        return DP[1][n]
        
