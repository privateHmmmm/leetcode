# -*- coding:utf-8 -*-


# Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.  You may assume the given string consists of lowercase English letters only and its length  will not exceed 10000. 
#
# Example 1:
#
# Input: "abab"
#
# Output: True
#
# Explanation: It's the substring "ab" twice.
#
#
#
# Example 2:
#
# Input: "aba"
#
# Output: False
#
#
#
# Example 3:
#
# Input: "abcabcabcabc"
#
# Output: True
#
# Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
#
#


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        # calculate s's next array
        nlen = len(s)
        _next = [-1 for i in range(0, nlen+1)]
        
        k = -1
        j = 0
        while j < len(s):
            if k == -1 or s[k] == s[j]:
                k += 1
                j += 1
                _next[j] = k
            else:
                k = _next[k]

        pattern = nlen - _next[nlen]
        if pattern == nlen: return False
        if nlen % pattern == 0: 
            return True
        else: 
            return False

