# -*- coding:utf-8 -*-


# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces  .
#
# You may assume that the given expression is always valid.
#
# Some examples:
#
# "1 + 1" = 2
# " 2-1 + 2 " = 3
# "(1+(4+5+2)-3)+(6+8)" = 23
#
#
#
#
# Note: Do not use the eval built-in library function.
#


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        res = 0
        sign = 1
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                while (i+1)<len(s) and s[i+1].isdigit():
                    num = num*10 + int(s[i+1])
                    i +=1
                res += num*sign
            elif s[i] == '+':
                sign = 1
            elif s[i] == '-':
                sign = -1
            elif s[i] == '(':
                stack.append(res)
                stack.append(sign)
                sign = 1
                res = 0
            elif s[i] == ')':
                res = res*stack.pop() + stack.pop()
            else:
                pass
            i +=1
        
        return res
                
