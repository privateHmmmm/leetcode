# -*- coding:utf-8 -*-


# Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.
#
# A student attendance record is a string that only contains the following three characters:
#
#
#
# 'A' : Absent. 
# 'L' : Late.
#  'P' : Present. 
#
#
#
#
# A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
#
# Example 1:
#
# Input: n = 2
# Output: 8 
# Explanation:
# There are 8 records with length 2 will be regarded as rewardable:
# "PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" won't be regarded as rewardable owing to more than one absent times. 
#
#
#
# Note:
# The value of n won't exceed 100,000.
#
#
#
#


class Solution(object):
    def checkRecord(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        """
        def sum(Lists):
            
            ans = 0
            for i in range(0, len(Lists)):
                ans += Lists[i]
            return ans % 1000000007
        
        
        DP = [[[ 0 for i in range(0, 3) ] for j in range(0, 2)] for k in range(0, n+1)]
        
        DP[1][0][0] = 1
        DP[1][0][1] = 1
        DP[1][0][2] = 0
        DP[1][1][0] = 1
        DP[1][1][1] = 0
        DP[1][1][2] = 0
        
        for i in range(2, n+1):
            DP[i][0][0] = sum(DP[i-1][0])
            DP[i][0][1] = DP[i-1][0][0]
            DP[i][0][2] = DP[i-1][0][1]
            DP[i][1][0] = (sum(DP[i-1][0]) + sum(DP[i-1][1])) % 1000000007
            DP[i][1][1] = DP[i-1][1][0]
            DP[i][1][2] = DP[i-1][1][1]
            
        return ( sum(DP[n][0]) + sum(DP[n][1])) % 1000000007
        """
    
    
        # dp[i] the number of all possible attendance (without 'A') records with length i:
        # end with "P": dp[i-1]
        # end with "PL": dp[i-2]
        # end with "PLL": dp[i-3]
        # end with "LLL": is not allowed
        # so dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
        if n == 1:
            return 3
        if n == 0:
            return 0
        DP = [1, 1, 2]
        i = 2
        while i < n:
            DP.append((DP[i] + DP[i-1] + DP[i-2])% 1000000007)
            i += 1
        result = (DP[n] + DP[n-1] + DP[n-2]) % 1000000007
        for i in range(n):
            result += DP[i+1] * DP[n-i] % 1000000007
            result %= 1000000007
        return result
        
        
        
        
        
        
