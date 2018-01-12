# -*- coding:utf-8 -*-


#
# Given a string S, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.
#
#
# For example: 
# Given "aacecaaa", return "aaacecaaa".
# Given "abcd", return "dcbabcd".
#
# Credits:Special thanks to @ifanchu for adding this problem and creating all test cases. Thanks to @Freezen for additional test cases.


class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # O(n) KMP
        
        # c  a  t  a  c  b  #  b  c  a  t  a  c
        # -1 0  0  0  0  1  0  0  0  1  2  3  4  5
    
        def _next(s):
            
            _next = [0 for i in range(0, len(s)+1)]
            _next[0] = -1
            
            j, k = -1, 0
            while k <= len(s)-1:
                if j == -1 or s[j] == s[k]:
                    j += 1
                    k += 1
                    _next[k] = j
                else:
                    j = _next[j]
            return _next
        
        extendS = s + '#' + s[::-1]
        _next = _next(extendS)
        
        return s[_next[-1]:][::-1] + s
        
