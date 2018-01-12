# -*- coding:utf-8 -*-


# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        def str2num(s):    
            return ord(s)-ord('0')
        
        res = ""
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        while i >=0 or j >=0 or carry == 1:
            a = str2num(num1[i]) if i >=0 else 0
            b = str2num(num2[j]) if j >=0 else 0 
            _sum = a+b+carry
            res+=str(_sum%10)
            carry = _sum/10
            i -= 1
            j -= 1
        
        return res[::-1]
