# -*- coding:utf-8 -*-


#
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true.
# Given num = 5, return false.
#
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:Special thanks to @yukuairoy  for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        
#         t = math.log(num, 4)
#         t1 = math.ceil(t)
#         t2 = math.floor(t)
        
#         return 4**t1 == num or num == 4**t2

        return math.log(num, 4) % 1 == 0
        
        # return n&(n-1)==0 and 
