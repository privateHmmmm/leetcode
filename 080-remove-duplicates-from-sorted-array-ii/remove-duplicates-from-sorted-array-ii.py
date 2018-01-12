# -*- coding:utf-8 -*-


#
# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
#


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        """
        def swapNum(i, j):
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
        
        
        start_index = 0
    
        i = 0
        while i < len(nums):
            if i+2 < len(nums) and nums[i] == nums[i+2]:
                swap = 2
                total = 3
                while i+total < len(nums) and nums[i] == nums[i+total]:
                    total = total + 1
                
            elif i + 1 < len(nums) and nums[i] == nums[i+1]:
                total = 2
                swap = 2
            else:
                total = 1
                swap = 1
                
            if start_index != 0:
                nums[start_index] = nums[i]
                if swap == 2:
                    nums[start_index + 1] = nums[i+1]
            
            if total > 2 or start_index != 0:
                if start_index == 0:
                    start_index = i + swap
                else:
                    start_index = start_index + swap

            i = i + total 
        
        return start_index if start_index > 0 else len(nums)
        """
        
        i = 0
        for n in nums:
            if i < 2 or nums[i-2] < n:
                nums[i] = n
                i+=1
        
        return i
