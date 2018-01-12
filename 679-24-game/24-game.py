# -*- coding:utf-8 -*-


#
# You have 4 cards each containing a number from 1 to 9.  You need to judge whether they could operated through *, /, +, -, (, ) to get the value of 24.
#
#
# Example 1:
#
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#
#
#
# Example 2:
#
# Input: [1, 2, 1, 2]
# Output: False
#
#
#
# Note:
#
# The division operator / represents real division, not integer division.  For example, 4 / (1 - 2/3) = 12.
# Every operation done is between two numbers.  In particular, we cannot use - as a unary operator.  For example, with [1, 1, 1, 1] as input, the expression -1 - 1 - 1 - 1 is not allowed.
# You cannot concatenate numbers together.  For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.
#
#
#


import itertools
class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        """
        # solution one, too complicate
        def evaluate(equ):
            
            if len(equ) == 1:
                return abs(float(equ[0]) - 24) < 0.0001
            
            for i in range(0, len(equ)-1, 2):
                try:
                    # avoid a division by zero
                    if evaluate(equ[:i] + [str(eval("".join(equ[i:i+3])))] + equ[i+3:]) == True:
                        # print equ
                        return True
                except:
                    pass
                
            return False
        
        numPermu = list(set(itertools.permutations([str(num)+'.0' for num in nums], 4)))
        operPermu = list(set(itertools.permutations("+++---***///", 3)))
        
        # print numPermu, operPermu, len(numPermu), len(operPermu)
        
        equ = [0] * (len(numPermu[0]) + len(operPermu[0]))
        for nums in numPermu:
            for opers in operPermu:
                for i, num in enumerate(nums):
                    equ[2*i] = num
                for i, oper in enumerate(opers):
                    equ[1+2*i] = oper
                
                # print equ
                if True == evaluate(equ):
                    return True
                
        return False
        """
        
        from itertools import permutations


        for per in permutations(nums):
            r = self.results(per)
            for x in r:
                if abs(x - 24) < 0.00000001:
                    return True
        return False

    def results(self, nums):
        if len(nums) == 1:
            return nums
        ret = set()
        for i in range(1, len(nums)):
            a = self.results(nums[:i])
            b = self.results(nums[i:])
            for x in a:
                for y in b:
                    ret.add(x + y)
                    ret.add(x - y)
                    ret.add(x * y)
                    if y != 0:
                        ret.add(x / float(y))
        # print nums, ret
        return ret
        
