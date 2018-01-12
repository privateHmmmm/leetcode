# -*- coding:utf-8 -*-


#
# Given an unsorted integer array, find the first missing positive integer.
#
#
#
# For example,
# Given [1,2,0] return 3,
# and [3,4,-1,1] return 2.
#
#
#
# Your algorithm should run in O(n) time and uses constant space.
#


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        # one good solution
        lens = len(nums)
        i = 0
        
        while i < lens:
            if nums[i] < (i+1) or nums[i] > lens:
                nums[i] = nums[lens-1]
                lens -=1
            elif nums[i] > (i+1):
                if nums[nums[i]-1] != nums[i]: 
                    tmp = nums[nums[i]-1]
                    nums[nums[i]-1] = nums[i]
                    nums[i] = tmp
                else:
                    del nums[i]
                    lens -=1
            else:
                i +=1
        
        return i + 1
        """
        
        a = 0
        i = 0
        lens = len(nums)
        
        while i < lens:
            if nums[i] > 0:
                a |= (1<<(nums[i]-1))
            i +=1
            
        i = 1
        while 1:
            if (a&1) == 0:
                return i
            else:
                a = a>>1
                i +=1
        
        
