# -*- coding:utf-8 -*-


# Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.
#
# Example 1
# Input: "2-1-1". 
# ((2-1)-1) = 0
# (2-(1-1)) = 2
# Output: [0, 2]
#
# Example 2
# Input: "2*3-4*5" 
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
# Output: [-34, -14, -10, -10, 10] 
#
# Credits:Special thanks to @mithmatt for adding this problem and creating all test cases.


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        
        res = []
        
        for i in range(0, len(input)):
            if input[i] in ['-', '+', '*']:
                l1 = self.diffWaysToCompute(input[0:i])
                l2 = self.diffWaysToCompute(input[i+1:])
                for num1 in l1:
                    for num2 in l2:
                        if input[i] == '-':
                            res.append(num1-num2)
                        elif input[i] == '+':
                            res.append(num1+num2)
                        else:
                            res.append(num1*num2)
        
        if len(res) == 0: res.append(int(input))
        return res
                    
        
