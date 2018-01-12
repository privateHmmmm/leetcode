# -*- coding:utf-8 -*-


# Given a non-negative integer n, count all numbers with unique digits, x, where 0 &le; x &lt; 10n.
#
#
#     Example:
# Given n = 2, return 91. (The answer should be the total numbers in the range of 0 &le; x &lt; 100, excluding [11,22,33,44,55,66,77,88,99])
#
#
# Credits:Special thanks to @memoryless for adding this problem and creating all test cases.


class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # another
        # f(1) = 10 (0, 1, 2, 3, ...., 9)
        # f(2) = 9 * 9
        # f(3) = f(2) * 8 = 9 * 9 * 8
        # f(4) = f(3) * 7 = 9 * 9 * 8 * 7
        # ...
        # f(10) = 9 * 9 * 8 * 7 * 6 * ... * 1
        # f(11) = 0 = f(12) = f(13)....
            
        # return f(1)+f(2)+f(3)+...+f(n)
        
        if n == 0: return 1
        n -= 1
        res = 10
        available_num = 9
        unique_digit = 9
        while n:
            unique_digit *= available_num
            res += unique_digit
            if available_num > 0: available_num -= 1
            n -= 1
        
        return res
            
