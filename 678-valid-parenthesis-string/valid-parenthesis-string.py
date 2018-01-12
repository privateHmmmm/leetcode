# -*- coding:utf-8 -*-


#
# Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        def check(s, stack):
        
            index = 0 
            while index < len(s):
                char = s[index]
                if char == '(':
                    stack.append(char)
                elif char == '*':
                    stack1 = copy.copy(stack)
                    stack2 = copy.copy(stack)
                    return check(s[index+1:], stack) or check('('+s[index+1:], stack1) or check(')'+s[index+1:], stack2)    
                elif char == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                    return False
                index += 1
                
            return stack == ["*"] * len(stack)
        
        stack = []
        return check(s, stack)
        """
        
        low = 0
        high = 0
        
        for i in range(0, len(s)):
            if s[i] == '(':
                low +=1
                high +=1
            elif s[i] == ')':
                if low>0:
                    low -=1
                high -=1
            else:
                if low>0:
                    low -=1
                high+=1
                
            if high < 0:
                return False

        return low == 0
                
