# -*- coding:utf-8 -*-


#
# Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#
#
#
# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#
#
#
# Note:
# You are not suppose to use the library's sort function for this problem.
#
#
# click to show follow up.
#
#
# Follow up:
# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with an one-pass algorithm using only constant space?
#
#


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        
        
        
        def swap(i, j):
            
            tmp = nums[i]
            nums[i] = nums[j]
            nums[j] = tmp 
        
        """
        # it's also good, but a lillte complex
        index1 = -1 # 第一个是1的数
        index2 = len(nums) - 1  # 第一个不是2的数
        i = 0
        while i <= index2: 
            
            if nums[i] == 0:
                if nums[index1] == 1:
                    swap(index1, i)
                    index1 += 1
                i += 1
                    
            elif nums[i] == 1:
                if index1 == -1:
                    index1 = i
                i += 1
                
            elif nums[i] == 2:
                for j in range(index2, i-1, -1):
                    if nums[j] != 2:
                        break
                index2 = j
                
                if index2 == i:
                    break
                else:
                    swap(index2, i)
                    index2 -= 1
                
        return
        """

#         index1=0
#         index2=len(nums)-1

#         i=0
#         while i <= index2:
#             if nums[i] == 0:
#                 if i > index1: swap(index1, i)
#                 index1 +=1
#                 i +=1
#             elif nums[i] == 2:
#                 if i < index2: swap(index2, i)
#                 index2 -=1
#             else:
#                 i+=1
                
#         return
    
    
        begin = 0; cur = 0; end = len(nums)-1
        while cur <= end:
            if nums[cur] == 1: 
                cur +=1
            elif nums[cur] == 0:
                if begin != cur:
                    swap(begin, cur)
                begin +=1
                cur +=1
            else:
                swap(cur, end)
                end -=1
                
                
