# -*- coding:utf-8 -*-


# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
#
#
#
# Credits:Special thanks to @Shangrila for adding this problem and creating all test cases.


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        
        # 0 , + , -
        # 整数
        # 小数
        if numerator == 0: return "0"
        res = "-" if ((numerator > 0) ^ (denominator > 0)) > 0 else ""
        
        numerator, denominator = abs(numerator), abs(denominator)
        res += (str(numerator/denominator))
        numerator %= denominator
        
        if numerator == 0: return res
        res += "."
        _map = {numerator: len(res)}
        
        while numerator != 0:
            numerator *= 10
            res += (str(numerator/denominator))
            numerator %= denominator
            if numerator in _map:
                index = _map[numerator]
                res = res[0:index] + '(' + res[index:] + ')'
                break
            _map[numerator] = len(res)
        
        return res
        
