# -*- coding:utf-8 -*-


# Given a string, determine if a permutation of the string could form a palindrome.
#
# For example,
# "code" -> False, "aab" -> True, "carerac" -> True.
#


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        count = collections.Counter(s)
        single = True
        
        for v in count.values():
            if v % 2 == 1:
                if single == False:
                    return False
                else:
                    single = False
        
        return True
        
