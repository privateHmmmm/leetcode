# -*- coding:utf-8 -*-


# Determine whether an integer is a palindrome. Do this without extra space.
#
# click to show spoilers.
#
# Some hints:
#
# Could negative integers be palindromes? (ie, -1)
#
# If you are thinking of converting the integer to string, note the restriction of using extra space.
#
# You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
#
# There is a more generic way of solving this problem.
#
#


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
     
#         def inverse(x):

#             res = 0
#             while x:
#                 res = res*10+x%10
#                 x = x/10
#             return res
        
#         if x < 0: return False
#         return x == inverse(x)

        if x < 0 or (x !=0 and x%10 == 0): return False # !!!!!
    
        res = 0
        while x > res: # !!!!
            res = res*10+(x%10)
            x = x/10
        
        return x==res or x == res/10
                
