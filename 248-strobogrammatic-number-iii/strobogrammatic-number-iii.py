# -*- coding:utf-8 -*-


# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.
# For example,
# Given low = "50", high = "100", return 3. Because 69, 88, and 96 are three strobogrammatic numbers.
#
#
# Note:
# Because the range might be a large number, the low and high numbers are represented as string.
#


class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        
        def helper(cur, _max):
            
            if cur == 0: return [""]
            if cur == 1: return ["0", "1", "8"]
            
            res = []
            center = helper(cur - 2, _max)
            for i in range(0, len(center)):
                if cur != _max:
                    res.append("0" + center[i] + "0")
                res.append("1" + center[i] + "1")
                res.append("8" + center[i] + "8")
                res.append("6" + center[i] + "9")
                res.append("9" + center[i] + "6")
            
            return res
        
        _list = []
        for i in range(len(low), len(high)+1):
            _list += helper(i, i)
        
        res = 0
        for num in _list:
            if (len(num) == len(low)) and num<low or (len(num) == len(high) and num > high): continue
            res +=1
        
        return res
        
