# -*- coding:utf-8 -*-


#
# Given two binary strings, return their sum (also a binary string).
#
#
#
# For example,
# a = "11"
# b = "1"
# Return "100".
#


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        i, j = len(a)-1, len(b)-1
        carry = 0
        res = ""
        
        while i>=0 or j >=0 or carry:
            _sum = carry
            if i >= 0: 
                _sum += int(a[i])
                i -= 1
            if j >= 0: 
                _sum += int(b[j])
                j -= 1
            res += str(_sum%2)
            carry = _sum/2
        
        res = res[::-1]
        return res
