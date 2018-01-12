# -*- coding:utf-8 -*-


#
# Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.
#
#
# Example1:
#
# a = 2
# b = [3]
#
# Result: 8
#
#
#
# Example2:
#
# a = 2
# b = [1,0]
#
# Result: 1024
#
#
#
# Credits:Special thanks to @Stomach_ache for adding this problem and creating all test cases.


class Solution(object):
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        
        
        def power(x, y):
            
            if y == 0:
                return 1
            elif y == 1:
                return x % 1337 
            
            return power(x, y / 2)**2 * power(x, y - y / 2 * 2) % 1337
        
        res = 1
        for i in range(0, len(b)):
            res = power(res, 10)*power(a, b[i]) % 1337
        return res
