# -*- coding:utf-8 -*-


# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
#
# Example:
# Given a = 1 and b = 2, return 3.
#
#
# Credits:Special thanks to @fujiaozhu for adding this problem and creating all test cases.


class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        
        #"""
        sum=0
        carry=0
        
        for i in range(0, 32):
            bitA=a&(1<<i)
            bitB=b&(1<<i)
            
            if bitA and bitB and carry:
                carry=1
                sum |= (1<<i)
            elif (bitA and carry) or (bitB and carry) or (bitA and bitB):
                carry=1
            elif bitA or bitB or carry:
                sum |= (1<<i)
                carry=0
            else:
                carry=0
        
        return sum if sum<=0x7fffffff else ~(sum ^ 0xffffffff)
        #"""
    
        # 0 + 0 = 00   ^
        # 0 + 1 = 01   ^
        # 1 + 0 = 01   ^
        # 1 + 1 = 10   &
        
    
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)
        """

