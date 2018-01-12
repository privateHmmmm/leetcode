# -*- coding:utf-8 -*-


#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
#
# The replacement must be in-place, do not allocate extra memory.
#
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 1,2,3 &#8594; 1,3,2
# 3,2,1 &#8594; 1,2,3
# 1,1,5 &#8594; 1,5,1
#


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # last increasing, small big, swap, reverse
        
        def swap(i, j):
            
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp
            
        # def reve
        
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]: 
                break
        else:
            nums[::] = nums[::-1]
            return
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j] > nums[i]:
                break
        
        swap(i, j)
        # print nums[i+1:j+1]
        nums[i+1:] = nums[i+1:][::-1]
        
