# -*- coding:utf-8 -*-


#
# Divide two integers without using multiplication, division and mod operator.
#
#
# If it is overflow, return MAX_INT.
#


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        # sign, overflow, divisor == 0
        _MAX, _MIN = 2**31-1, -2**31
        if divisor == 0: return _MAX
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        
        dvd, dvs = abs(dividend), abs(divisor)
        res = 0
        while dvd >= dvs:
            _sum = dvs
            mul = 1
            while dvd - (_sum<<1) >= 0:
                _sum <<= 1
                mul <<= 1
            res += mul
            dvd -= _sum
        
        if res > _MAX:
            return _MAX if sign == 1 else _MIN
        else:
            return sign*res  
            
