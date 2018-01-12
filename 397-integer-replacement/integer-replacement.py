# -*- coding:utf-8 -*-


#
# Given a positive integer n and you can do operations as follow:
#
#
#
#
# If n is even, replace n with n/2.
# If n is odd, you can replace n with either n + 1 or n - 1.
#
#
#
#
# What is the minimum number of replacements needed for n to become 1?
#
#
#
#
# Example 1:
#
# Input:
# 8
#
# Output:
# 3
#
# Explanation:
# 8 -> 4 -> 2 -> 1
#
#
#
# Example 2:
#
# Input:
# 7
#
# Output:
# 4
#
# Explanation:
# 7 -> 8 -> 4 -> 2 -> 1
# or
# 7 -> 6 -> 3 -> 2 -> 1
#
#


class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # 如果倒数第二位是0，那么n-1的操作比n+1的操作能消掉更多的1
        # 1001 - 1 = 1000； 1001 + 1 = 1010
        # 如果倒数第二位是1，那么n+1的操作比n-1的操作能消掉更多的1
        # 1111 + 1 = 10000；1111 - 1 = 1110
        
        res = 0
        
        while n > 1:
            res += 1
            if n % 2 == 0:
                n = n >>1
            else:
                if n == 3:
                    return res + 1
                else:
                    if n & 2 == 2:
                        n = n + 1
                    else:
                        n = n - 1
        
        return res
    
