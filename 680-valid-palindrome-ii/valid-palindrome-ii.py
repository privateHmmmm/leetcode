# -*- coding:utf-8 -*-


#
# Given a non-empty string s, you may delete at most one character.  Judge whether you can make it a palindrome.
#
#
# Example 1:
#
# Input: "aba"
# Output: True
#
#
#
# Example 2:
#
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
#
#
#
# Note:
#
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
#
#


class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        def isPalindrome(s):
        
            return s[::-1] == s
        
        for i in range(0, len(s)):
            if s[i] != s[len(s)-1-i]:
                return isPalindrome(s[i+1:len(s)-i]) or isPalindrome(s[i:len(s)-1-i])
            
        return True
