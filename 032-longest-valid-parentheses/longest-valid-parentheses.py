# -*- coding:utf-8 -*-


# Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
#
#
# For "(()", the longest valid parentheses substring is "()", which has length = 2.
#
#
# Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
#


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        start = -1
        max_len = 0
        
        for i in range(0, len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    node = stack.pop()
                    if stack:
                        max_len = max(max_len, i-stack[-1])
                    else:
                        max_len = max(max_len, i-start)
                else:
                    start = i
        
        return max_len
            
