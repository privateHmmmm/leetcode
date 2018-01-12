# -*- coding:utf-8 -*-


# Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.
#
# Note:
#
# The length of both num1 and num2 is < 110.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
#
#


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        """
           index        0 1 2 3 4 
            num1            1 2 3                 index[i]
            num2              4 5                 index[j]     
                     ----------------
                              1 5
                            1 0
                          0 5
                     ----------------
                            1 2
                          0 8          indices[i+j, i+j+1]
                        0 4
                     ----------------
                        0 5 5 3 5
                index   0 1 2 3 4
        """
        
        if not num1 or not num2: return "0"
        
        digits = [0 for i in range(0, len(num1)+ len(num2))]
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                p1, p2 = i+j, i+j+1
                product = (ord(num1[i])-48)*(ord(num2[j])-48)
                _sum = digits[p2] + product
                digits[p2] = _sum%10
                digits[p1] += _sum/10
            
        res = "".join([str(d) for d in digits]).lstrip("0")
        return res if res else "0"
