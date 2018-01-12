# -*- coding:utf-8 -*-


#
# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
#
#
#
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        ones = 0
        twos = 0
        for i in range(0, len(nums)):
            ones = (ones ^ nums[i]) & ~twos
            twos = (twos ^ nums[i]) & ~ones
        
        return ones
        """
        
        
        """
        def convert(x):
            
            if x>=2**31:
                x-=2**32
            return x
            
        sum=0
        for i in range(0, 32):
            bit =0
            for num in nums:
                bit+=(num>>i)&1
            sum |= ((bit%3)<<i)
        
        return convert(sum)
        """
        
        ones=0
        twos=0
        threes=0
        
        for num in nums:
            twos |= (ones&num)
            ones ^=num
            threes = ones & twos
            ones ^=threes
            twos^= threes
        
        return ones
        
        
