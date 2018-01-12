# -*- coding:utf-8 -*-


# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
#


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        
        stack = []
        for i in range(0, len(s)):
            if s[i] in ['(', '{', '[']:
                stack.append(s[i])
            else:
                if stack and ((s[i] == ')' and stack[-1] == '(') or s[i] == '}' and stack[-1] == '{' or s[i] == ']' and stack[-1] == '['):
                    stack.pop()
                else:
                    return False
        
        return stack == []
       
