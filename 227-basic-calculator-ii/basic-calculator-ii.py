# -*- coding:utf-8 -*-


# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string contains only non-negative integers, +, -, *, / operators and empty spaces  . The integer division should truncate toward zero.
#
# You may assume that the given expression is always valid.
#
# Some examples:
#
# "3+2*2" = 7
# " 3/2 " = 1
# " 3+5 / 2 " = 5
#
#
#
#
# Note: Do not use the eval built-in library function.
#
#
# Credits:Special thanks to @ts for adding this problem and creating all test cases.


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        stack = []
        num = 0
        sign = '+'
        
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = int(s[i])
                while i+1 < len(s) and s[i+1].isdigit():
                    num = num*10+int(s[i+1])
                    i +=1
                    
            if s[i] != " ":
                if sign == '+':
                    stack.append(num)
                elif sign == '-':
                    stack.append(-num)
                elif sign == '*':
                    stack.append(stack.pop()*num)
                elif sign == '/':
                    # special handle for python nagative devide
                    num1 = stack.pop()
                    if num1 * num < 0:
                        stack.append(-(abs(num1)/abs(num)))
                    else:
                        stack.append(num1/num)
                else:
                    pass
                # num = 0
                sign = s[i]
            i += 1
    
        return sum(stack)
                    
