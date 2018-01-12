# -*- coding:utf-8 -*-


#
#     Given an integer, write a function to determine if it is a power of three.
#
#
#     Follow up:
#     Could you do it without using any loop / recursion?
#
#
# Credits:Special thanks to @dietpepsi for adding this problem and creating all test cases.


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        
        # if n <= 0:
            # return False
        # t=math.log(n,3)
        # t1=math.ceil(t)
        # t2=math.floor(t)
        # return 3**t1 == n or 3**t2 == n
    
        return ( n>0 and 1162261467%n==0);
