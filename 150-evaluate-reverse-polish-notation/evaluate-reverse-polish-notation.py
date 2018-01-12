# -*- coding:utf-8 -*-


#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
#
#
# Valid operators are +, -, *, /. Each operand may be an integer or another expression.
#
#
#
# Some examples:
#
#   ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
#   ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
#
#


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        
        stack = []
        
        for i in range(0, len(tokens)):
            if tokens[i] in ['+', '-', '*', '/']:
                p2 = stack.pop()
                p1 = stack.pop()
                if tokens[i] == '+':
                    stack.append(p1+p2)
                elif tokens[i] == '-':
                    stack.append(p1-p2)
                elif tokens[i] == '*':
                    stack.append(p1*p2)
                else:
                    if p1*p2>0:
                        stack.append(p1/p2)
                    else:
                        stack.append(abs(p1)/abs(p2)*-1)
            else:
                stack.append(int(tokens[i]))
        
        return stack[-1]

