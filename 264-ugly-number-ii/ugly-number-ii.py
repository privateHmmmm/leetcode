# -*- coding:utf-8 -*-


#
# Write a program to find the n-th ugly number.
#
#
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
#
#
#
# Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
#
#
# Credits:Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.


class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        l2, l3, l5 = 0, 0, 0
        
        res = [1]
        for i in range(1, n):
            Min = min(res[l2]*2, res[l3]*3, res[l5]*5)
            res.append(Min)
            if Min == res[l2]*2:
                l2 += 1
            if Min == res[l3]*3:
                l3 += 1
            if Min == res[l5]*5:
                l5 += 1
            
        return res[n-1]
