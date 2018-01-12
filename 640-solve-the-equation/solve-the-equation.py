# -*- coding:utf-8 -*-


#
# Solve a given equation and return the value of x in the form of string "x=#value". The equation contains only '+', '-' operation, the variable x and its coefficient.
#
#
#
# If there is no solution for the equation, return "No solution".
#
#
# If there are infinite solutions for the equation, return "Infinite solutions".
#
#
# If there is exactly one solution for the equation, we ensure that the value of x is an integer.
#
#
# Example 1:
#
# Input: "x+5-3+x=6+x-2"
# Output: "x=2"
#
#
#
# Example 2:
#
# Input: "x=x"
# Output: "Infinite solutions"
#
#
#
# Example 3:
#
# Input: "2x=x"
# Output: "x=0"
#
#
#
# Example 4:
#
# Input: "2x+3x-6x=x+2"
# Output: "x=-1"
#
#
#
# Example 5:
#
# Input: "x=x+2"
# Output: "No solution"
#
#


class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        
        
        coefficient = 0
        constance = 0
        
        index = 0
        sign = 1
        left = 1
        while index < len(equation):
            if equation[index] == '+':
                sign = 1*left
            elif equation[index] == '-':
                sign = -1*left
            elif equation[index] == '=':
                left = -1
                sign = 1*left
            elif equation[index] == 'x':
                coefficient += sign
            elif equation[index].isdigit() == True:
                i = index
                while i<len(equation) and equation[i].isdigit() == True:
                    i +=1
                    
                num = int(equation[index:i])
                if i < len(equation) and equation[i] == 'x':
                    coefficient += sign*num
                    index = i+1
                else:
                    constance += sign*num
                    index = i
                continue
            else:
                print "what's the hell ..."
                print equation[index]
            
            index +=1
            
        # print coefficient, constance
        if (not coefficient and constance):
            return "No solution"
        elif (not coefficient and not constance):
            return "Infinite solutions"
        else:
            return "x=%d" %(-constance/coefficient)
                
                
                
